Name : Abhinav
Roll number : 23110006

This website was developed using HTML,CSS,JS,ChartJS,flask,Bootstrap and djinja2. All the required dependencies can be found in requirements.txt.

First the data from the pdfs was extracted into two csv files, encashed_bonds_data and purchased_bonds_data using fitz. The code used to achieve this and the corresponding pdf and csv files can all be found in the PDF_TO_CSV folder.

In MySQL:


First a database called all_bonds_data was created.
Two tables caleed all_data_encashed adn all_data_purchased were created, and the data from the csv files were copied into these tables. A query was run on both tables to remove the commas from the denominations attribute and change its datatype to bigint.


All the queries used to setup and modify the table as described above can be found in the flask.sql file.

Website:


The website folder contains all the HTML templates and the main.py flask file. Note that all CSS and JS used is inline and there are seperate static files for these.

Steps to set up the website:


1. Download the sql dump and set up the testing user and password.The query to set up this user is given under SQL_DUMP folder. You can use any other user and password but make
   sure to change username and password accordingly in the main.py file.

2. RUn the main.py file and then load the address as shown in the terminal.

Home page of the website :

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/8df96871-1ecb-4373-a509-40279a6c7d61)

Answers to the questions with Images :

Question 1 :

The user is prompted to chose the table from which he wants to fetch the records from. The fields dropdown gets updated based on the choice of the table to correspond the fields of the selected table, this is achieved using embedded JS code. The user can then enter the value of the field and hit enter to fetch the records. Bootstap was added to make the table better looking.
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/a9689b99-c90b-45f5-a27c-1a4b76346e3c)

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/8d80840f-f11d-4c8b-aae7-21c1c71127b8)

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/bd1131a9-9b3f-4217-a751-0538e53db300)

The SQL query behind this can be found in the main.py file.

Question 2 :

For the second quesiton, the user is prompted to enter the name of the comapny for which they want to check the data for. After submitting it, a table is displayed contianing the year and the number of bonds purchased and their value as fields. Two bar charts are also plotted using ChartJS using the afforementioned fields. A fucntionality to downlaod the Charts is also added. The JS code for this embedded inline. Bootstap was to make the table better looking.

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/3c79dca3-cdf0-4be3-8824-d8bb2ea9fbeb)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/2fdc05b5-baf6-4815-bc63-c618c64b12cb)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/5481071a-d1ca-4085-875e-d4f235c2907e)

Question 3 :

For the third quesiton, the user is prompted to enter the name of the party for which they want to check the data for. After submitting it, a table is displayed contianing the year and the number of bonds purchased and their value as fields. Two bar charts are also plotted using ChartJS using the afforementioned fields. A fucntionality to downlaod the Charts is also added. The JS code for this embedded inline. Bootstap was added to make the table better looking.

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/9ce9e1c1-496b-4207-a6c0-33c4cb969f86)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/755a3146-7477-4472-b917-0fb3d0537437)

Question 4 :

For the fourth question, the user is prompted to enter the name of a poltitcal party. After submitting the name, an alluvial plot of the companies that donated to the party is shown. An option to download this chart is also given. A table showing the companies that donated to the party along with the total amount that the company donated to the party is given. The total amount donated to the party by all the companies is also displayed. The query for this task is performed on the inner join on the all_data_encashed and all_data_purchased table.

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/c00e07db-c463-4f54-962c-8e1377c047c2)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/22d30a6d-a916-4423-b42b-a4ce8f978aa7)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/5e75f79d-7924-4444-ba68-22f3c85c7539)

Question 5 :

For the fifth question, the user is prompted to enter the name of a company. After submitting the name, an alluvial plot of the parteies that the company donated to is shown. An option to download this chart is also given. A table showing the companies that donated to the party along with the total amount that the company donated to the party is given. The total amount donated by the company to different parties is also displayed. The query for this task is performed on the inner join on the all_data_encashed and all_data_purchased table.

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/a54103e8-bb29-4cc8-a308-d4f49eac4c62)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/457a0d5d-ff9b-4f13-8b11-71db238d169b)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/b3a7f996-a6dd-4339-bfda-b9ac25281c80)


Question 6 :

For the sixth question, a pie chart showing the distribution of donations to all political parties is shown. The chart is an interactive chart plotted using ChartJS and an option to download it is also given.

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/aefdaef5-fd0b-46e0-8112-b84079624677)









