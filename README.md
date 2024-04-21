Name : Abhinav
Roll number : 23110006

This website was developed using HTML,CSS,JS,ChartJS,flask,Bootstrap and djinja2. All the required dependencies can be found in requirements.txt

First the data from the pdfs was extracted into two csv files, encashed_bonds_data and purchased_bonds_data using fitz. The code used to achieve this and the corresponding pdf and csv files can all be found in the PDF_TO_CSV folder.

In MySQL:
\\

First a database called all_bonds_data was created.
\\

Two tables caleed all_data_encashed adn all_data_purchased were created, and the data from the csv files were copied into these tables. A query was run on both tables to remove the commas from the denominations attribute and change its datatype to bigint.
\\

All the queries used to setup and modify the table as described above can be found in the flask.sql file.

Website:
\\
The website folder contains all the HTML templates and the main.py flask file. Note that all CSS and JS used is inline and there are seperate static files for these.
\\
Steps to set up the website:
\\

1. Download the sql dump and set up the testing user and password. You can use any other user and password but make
   sure to change username and password accordingly in the main.py file.

2. RUn the main.py file and then load the address as shown in the terminal.

Home page of the website :

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/8df96871-1ecb-4373-a509-40279a6c7d61)

Answers to the questions with Images :

Question 1 :
