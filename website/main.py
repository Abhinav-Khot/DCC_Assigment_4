from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'testing'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'all_bonds_data'

mysql = MySQL(app)


@app.route("/")
def main_page():
    return render_template("mainpage.html")



@app.route('/filterpage')
def filter_page():
   return render_template('filterpage.html')

@app.route('/filterpage/result',methods = ['POST', 'GET'])
def result():
   data = 0
   if request.method == 'POST':
      result_ = request.form
      print(result_)
      cursor = mysql.connection.cursor()
      
      Encashed_fields = ["Bond_Number", "Name_of_the_Political_Party", "Date_of_Encashment", "Account_no_of_Political_Party", "Denominations","Pay_Branch_Code","Pay_Teller"]
      Purchased_fields = ["Bond_Number", "Name_of_the_Purchaser", "Date_of_Purchase", "Date_of_Expiry", "Journal_Date", "Issue_Branch_Code", "Issue_Teller", "Reference_Number_URN"]
      if result_["table_selecter"] == "Purchased":
         k = "Purchased"

         for i in Purchased_fields:
            if i == result_["Fields_Purchased"]:
                cursor.execute(f"select * from all_data_purchased where {i} = %s", (result_["Field_val"],))
                break
      else:
         k = "Encashed"
         for i in Encashed_fields:
            if i == result_["Fields_Encashed"]:
                cursor.execute(f"select * from all_data_encashed where {i} = %s", (result_["Field_val"],))
                break


      data = cursor.fetchall()
      cursor.close()
      if len(data) == 0:
         data = "NA"

      print(k)
      return render_template("filterpage.html",result = data, table = k )


@app.route("/company_purchases_year")
def company_purchases_year():
    return render_template('company_purchases_year.html')

@app.route("/company_purchases_year/result", methods = ['POST', 'GET'])
def comapany_purchases_year_result():
   if request.method == 'POST':
      result_ = request.form
      print(result_)
      cursor = mysql.connection.cursor()
      format = '%d/%M/%Y'
      print(f"SELECT year(STR_TO_DATE(Date_of_Purchase, '{format}')) AS Purchase_Year, SUM(Denominations) AS Total_Bond_Value FROM all_data_purchased WHERE Name_of_the_Purchaser = '{result_["Company_Name"]}' GROUP BY Purchase_Year")
      cursor.execute(f"SELECT year(STR_TO_DATE(Date_of_Purchase, '{format}')) AS Purchase_Year, SUM(Denominations) AS Total_Bond_Value,COUNT(Denominations) as Noofbonds FROM all_data_purchased WHERE Name_of_the_Purchaser = '{result_["Company_Name"]}' GROUP BY Purchase_Year")

      data = cursor.fetchall()
      cursor.close()
      print(data)
      if len(data) == 0:
         data = "NA"
      return render_template("company_purchases_year.html", result = data, cname = result_["Company_Name"])
   


@app.route("/party_encashment_year")
def party_encashment_year():
    return render_template('party_encashment_year.html')

@app.route("/party_encashment_year/result", methods = ['POST', 'GET'])
def party_encashment_year_result():
   if request.method == 'POST':
      result_ = request.form
      print(result_)
      cursor = mysql.connection.cursor()
      format = '%d/%M/%Y'
      cursor.execute(f"SELECT year(STR_TO_DATE(Date_of_Encashment, '{format}')) AS Encashed_Year, SUM(Denominations) AS Total_Bond_Value,COUNT(Denominations) as Noofbonds FROM all_data_encashed WHERE Name_of_the_Political_Party = '{result_["Party_Name"]}' GROUP BY Encashed_Year")

      data = cursor.fetchall()
      cursor.close()
      print(data)
      if len(data) == 0:
         data = "NA"
      return render_template("party_encashment_year.html", result = data, pname = result_["Party_Name"])
   

@app.route("/party_company_donation")
def party_company_donation():
   return render_template("party_company_donation.html")


@app.route("/party_company_donation/result", methods = ["POST", "GET"])
def party_company_donation_result():
    if request.method == 'POST':
      result_ = request.form
      cursor = mysql.connection.cursor()
      
      cursor.execute(f"select Name_of_the_Purchaser, sum(all_data_encashed.Denominations) as total_amount_donated from all_data_encashed join all_data_purchased on (all_data_encashed.Prefix,all_data_encashed.Bond_Number) = (all_data_purchased.Prefix, all_data_purchased.Bond_Number) where Name_of_the_Political_Party = '{result_["Party_Name"]}' group by Name_of_the_Purchaser")

      data = cursor.fetchall()
      cursor.close()
      cursor = mysql.connection.cursor()
      cursor.execute(f"select sum(all_data_encashed.Denominations) from all_data_encashed join all_data_purchased on (all_data_encashed.Prefix,all_data_encashed.Bond_Number) = (all_data_purchased.Prefix, all_data_purchased.Bond_Number) where Name_of_the_Political_Party = '{result_["Party_Name"]}'")
      data_1 = cursor.fetchall() 
      
      cursor.close()
      print(data_1)
      if len(data) == 0:
         data = "NA"
      return render_template("party_company_donation.html", result = data, pname = result_["Party_Name"], total = data_1)

@app.route("/company_to_party_donation")
def company_to_party_donation():
   return render_template("company_to_party_donation.html")


@app.route("/company_to_party_donation/result", methods = ["POST", "GET"])
def company_to_party_donation_result():
    if request.method == 'POST': 
      result_ = request.form
      print(result_)
      cursor = mysql.connection.cursor()
      
      cursor.execute(f"select Name_of_the_Political_Party, sum(all_data_encashed.Denominations) as total_amount_donated from all_data_encashed join all_data_purchased on (all_data_encashed.Prefix,all_data_encashed.Bond_Number) = (all_data_purchased.Prefix, all_data_purchased.Bond_Number) where Name_of_the_Purchaser = '{result_["Company_Name"]}' group by Name_of_the_Political_Party")

      data = cursor.fetchall()
      cursor.close()
      cursor = mysql.connection.cursor()
      cursor.execute(f"select sum(all_data_encashed.Denominations) as total_amount_donated from all_data_encashed join all_data_purchased on  (all_data_encashed.Prefix,all_data_encashed.Bond_Number) = (all_data_purchased.Prefix, all_data_purchased.Bond_Number) where Name_of_the_Purchaser = '{result_["Company_Name"]}' ")
      data_1 = cursor.fetchall() 
      
      cursor.close()
      print(data)
      print(data_1)
      if len(data) == 0:
         data = "NA"
      return render_template("company_to_party_donation.html", result = data, cname = result_["Company_Name"], total = data_1)
    


@app.route("/total_donations_pie")
def total_donations_pie():
   cursor = mysql.connection.cursor()

   cursor.execute("select Name_of_the_Political_Party, sum(Denominations) from all_data_encashed group by Name_of_the_Political_Party")

   data = cursor.fetchall()

   cursor.close()

   return render_template("total_donations_pie.html", result = data)

if __name__ == '__main__':
   app.run(debug = True)
 