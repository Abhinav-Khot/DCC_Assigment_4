Name : Abhinav
Roll number : 23110006

This website was developed using HTML,CSS,JS,ChartJS,flask,Bootstrap and djinja2. All the required dependencies can be found in requirements.txt

First the data from the pdfs was extracted into two csv files, encashed_bonds_data and purchased_bonds_data using fitz. The code used to achieve this and the corresponding pdf and csv files can all be found in the PDF_TO_CSV folder.

In MySQL:


First a database called all_bonds_data was created.


Two tables caleed all_data_encashed adn all_data_purchased were created, and the data from the csv files were copied into these tables. A query was run on both tables to remove the commas from the denominations attribute and change its datatype to bigint.


All the queries used to setup and modify the table as described above can be found in the flask.sql file.

Website:


The website folder contains all the HTML templates and the main.py flask file. Note that all CSS and JS used is inline and there are seperate static files for these.

Steps to set up the website:


1. Download the sql dump and set up the testing user and password. You can use any other user and password but make
   sure to change username and password accordingly in the main.py file.

2. RUn the main.py file and then load the address as shown in the terminal.

Home page of the website :

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/8df96871-1ecb-4373-a509-40279a6c7d61)

Answers to the questions with Images :

Question 1 :

The user is prompted to chose the table from which he wants to fetch the records from. The fields dropdown gets updated based on the choice of the table to correspond the fields of the selected table, this is achieved using embedded JS code. The user can then enter the value of the field and hit enter to fetch the records. Bootstap was to make the table better looking.
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/a9689b99-c90b-45f5-a27c-1a4b76346e3c)

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/8d80840f-f11d-4c8b-aae7-21c1c71127b8)

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/bd1131a9-9b3f-4217-a751-0538e53db300)

The SQL query behind this can be found in the main.py file. The Basic pesudocode outline is SELECT FIELD FROM TABLE WHERE FIELD_VALUE = USER_ENTERED_TABLE;

Question 2 :

For the second quesiton, the user is prompted to enter the name of the comapny for which they want to check the data for. After submitting it, a table is displayed contianing the year and the number of bonds purchased and their value as fields. Two bar charts are also plotted using ChartJS using the afforementioned fields. A fucntionality to downlaod the Charts is also added. The JS code for this embedded inline. Bootstap was to make the table better looking.

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/3c79dca3-cdf0-4be3-8824-d8bb2ea9fbeb)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/2fdc05b5-baf6-4815-bc63-c618c64b12cb)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/5481071a-d1ca-4085-875e-d4f235c2907e)







