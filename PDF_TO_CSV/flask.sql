create database all_bonds_data;


use all_bonds_data;

CREATE TABLE all_data_encashed (
  Sr_No BIGINT PRIMARY KEY, 
  Date_of_Encashment VARCHAR(20),
  Name_of_the_Political_Party VARCHAR(100) NOT NULL,
  Account_no_of_Political_Party VARCHAR(20) NOT NULL,
  Prefix VARCHAR(10) NOT NULL,
  Bond_Number BIGINT,
  Denominations VARCHAR(20),
  Pay_Branch_Code VARCHAR(10),
  Pay_Teller BIGINT	
);
-- after making above table execute the below
set sql_safe_updates = 0;
update all_data_encashed set denominations = replace(denominations, ",", "");
alter table all_data_encashed modify column denominations bigint;



CREATE TABLE all_data_purchased (
  Sr_No BIGINT PRIMARY KEY,  
  `Reference_Number_URN` VARCHAR(70),
  Journal_Date VARCHAR(20) ,
  Date_of_Purchase date,
  Date_of_Expiry date,
  Name_of_the_Purchaser VARCHAR(100),
  Prefix VARCHAR(10) NOT NULL,
  Bond_Number BIGINT,
  Denominations VARCHAR(20),
  Issue_Branch_Code BIGINT,
  Issue_Teller BIGINT,
  `Status` VARCHAR(10)
);
-- after making above table execute the below
set sql_safe_updates = 0;
update all_data_purchased set denominations = replace(denominations, ",", "");
alter table all_data_purchased modify column denominations bigint;

-- ----------------------


select Name_of_the_Purchaser, sum(all_data_encashed.Denominations) as total_amount_donated from all_data_encashed join all_data_purchased on 
(all_data_encashed.Prefix,all_data_encashed.Bond_Number) = 
(all_data_purchased.Prefix, all_data_purchased.Bond_Number) group by Name_of_the_Purchaser;


select  (sum(all_data_encashed.Denominations)) as total_amount_donated from all_data_encashed join all_data_purchased on 
(all_data_encashed.Prefix,all_data_encashed.Bond_Number) = 
(all_data_purchased.Prefix, all_data_purchased.Bond_Number);

select Name_of_the_Political_Party,sum(all_data_encashed.Denominations) from all_data_encashed join all_data_purchased on 
(all_data_encashed.Prefix,all_data_encashed.Bond_Number) = 
(all_data_purchased.Prefix, all_data_purchased.Bond_Number) group by Name_of_the_Political_Party;


select Name_of_the_Political_Party, sum(all_data_encashed.Denominations) as total_amount_donated from all_data_encashed join all_data_purchased on 
(all_data_encashed.Prefix,all_data_encashed.Bond_Number) = 
(all_data_purchased.Prefix, all_data_purchased.Bond_Number) where Name_of_the_Purchaser = "BHARTI AIRTEL LIMITED" group by Name_of_the_Political_Party;


select Name_of_the_Purchaser,sum(all_data_encashed.Denominations) from all_data_encashed join all_data_purchased on 
(all_data_encashed.Prefix,all_data_encashed.Bond_Number) = 
(all_data_purchased.Prefix, all_data_purchased.Bond_Number) where Name_of_the_Political_Party = "", group by Name_of_the_Purchaser;

select sum(all_data_encashed.Denominations) from all_data_encashed join all_data_purchased on (all_data_encashed.Prefix,all_data_encashed.Bond_Number) = (all_data_purchased.Prefix, all_data_purchased.Bond_Number) where Name_of_the_Purchaser = 'bharti airtel limited';

select * from all_data_encashed;
select * from all_data_purchased;
 
 select count(distinct Name_of_the_Political_Party) from all_data_encashed;