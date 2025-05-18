# Electoral Bonds Data Analysis Portal

A web application for analyzing and visualizing electoral bonds data in India, showing the financial relationships between companies and political parties.

![Home page](https://github.com/NiTr0z0/flask_practice/assets/162600608/8df96871-1ecb-4373-a509-40279a6c7d61)

## Overview

This project presents electoral bonds data through an interactive web interface that allows users to:
- Search and filter bond data by various parameters
- Visualize company donations over time 
- Analyze political party funding sources
- Explore the relationships between donors and recipients
- View overall donation distribution across political parties
- Download all visualizations

## Technologies Used

- **Backend**: Flask, MySQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Data Visualization**: Chart.js
- **Data Processing**: fitz for PDF to CSV conversion, MySQL for data cleaning

## Features

### Data Search & Filtering
Users can search records from either the encashed or purchased bonds tables by selecting fields and entering search terms.

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/8d80840f-f11d-4c8b-aae7-21c1c71127b8)

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/bd1131a9-9b3f-4217-a751-0538e53db300)

![image](https://github.com/NiTr0z0/DCC_Assigment_4/assets/162600608/e0b3b69b-7280-44fa-a32f-5781e72495ff)

![image](https://github.com/NiTr0z0/DCC_Assigment_4/assets/162600608/e824f263-1c60-4b61-a344-1a7a591884e1)

### Company Donation Analysis
View time-series data of bonds purchased by a specific company, including visualization of both bond counts and monetary values.

![Company analysis](https://github.com/NiTr0z0/flask_practice/assets/162600608/5481071a-d1ca-4085-875e-d4f235c2907e)

### Political Party Funding Analysis
Examine bonds encashed by a specific political party over time, with visualizations of both bond counts and monetary values.

![Party analysis](https://github.com/NiTr0z0/flask_practice/assets/162600608/755a3146-7477-4472-b917-0fb3d0537437)

### Donation Flow Visualization
Interactive alluvial diagrams showing the flow of funds from companies to political parties.

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/c00e07db-c463-4f54-962c-8e1377c047c2)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/22d30a6d-a916-4423-b42b-a4ce8f978aa7)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/5e75f79d-7924-4444-ba68-22f3c85c7539)

![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/a54103e8-bb29-4cc8-a308-d4f49eac4c62)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/457a0d5d-ff9b-4f13-8b11-71db238d169b)
![image](https://github.com/NiTr0z0/flask_practice/assets/162600608/b3a7f996-a6dd-4339-bfda-b9ac25281c80)

### Overall Distribution
Pie chart showing the distribution of all electoral bond funds across political parties.

![Distribution chart](https://github.com/NiTr0z0/flask_practice/assets/162600608/aefdaef5-fd0b-46e0-8112-b84079624677)

## Installation & Setup

1. Clone the repository
2. Set up MySQL and import the SQL dump from the `SQL_DUMP` folder
3. Create a database user (or use the provided test user setup)
```sql
CREATE USER 'testing'@'%' IDENTIFIED BY 'password'; 
GRANT ALL PRIVILEGES ON *.* TO 'testing'@'%' WITH GRANT OPTION;
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```
5. Run the application:
```
python main.py
```

## Error Handling

The application includes robust error handling for cases when no data is found for a search query:

![image](https://github.com/NiTr0z0/DCC_Assigment_4/assets/162600608/3e931c4d-6945-4244-b448-e91d4d33581c)
![image](https://github.com/NiTr0z0/DCC_Assigment_4/assets/162600608/c825f5fa-d839-4f4d-a10b-a858b08e3f02)

![image](https://github.com/NiTr0z0/DCC_Assigment_4/assets/162600608/0bd9a20d-8a4d-4b89-ba03-99fa84abeb21)
![image](https://github.com/NiTr0z0/DCC_Assigment_4/assets/162600608/b936927e-fbcc-4d28-b41c-0d17bd36b0fa)
