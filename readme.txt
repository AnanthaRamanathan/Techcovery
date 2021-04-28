CREATE DATABASE app;

use app;

CREATE TABLE users (
  name varchar(255),
  email varchar(255) NOT NULL,
  confirm_email varchar(255),
  password varchar(255) NOT NULL
);

#Create user
curl http://localhost:5000/create/ram,ramemail,rampassword
#Read user
curl http://localhost:5000/read/ramemail
#Delete user
curl http://localhost:5000/delete/ramemail


CREATE TABLE users_info (
name varchar(255),
Your_desired_start_up varchar(255),
my_email varchar(255),
retype_email varchar(255),
password varchar(255),
education varchar(255),
from_ varchar(255),
in_ varchar(255),

My_Expected_compensation varchar(255),
Your_Linkedin_Profile varchar(255),
Im_a varchar(255),
My_expertise_lies_in varchar(255),
My_Core_competencies varchar(255),

My_Work_Experience varchar(255),
My_Mobile_number varchar(255),
My_Current_Employer varchar(255),
Im_available_in varchar(255)

);

name, Your_desired_start_up, my_email, retype_email, password, education, from_, in_, My_Expected_compensation, Your_Linkedin_Profile, Im_a,My_expertise_lies_in, My_Core_competencies, My_Work_Experience,My_Mobile_number, My_Current_Employer, Im_available_in


<name>, <Your_desired_start_up>, <my_email>, <retype_email>, <password>, <education>, <from_>, <in_>, <My_Expected_compensation>, <Your_Linkedin_Profile>, <Im_a>,<My_expertise_lies_in>, <My_Core_competencies>, <My_Work_Experience>,<My_Mobile_number>, <My_Current_Employer>, <Im_available_in>

CREATE TABLE user_details (
name varchar(255),
Your_desired_start_up varchar(255),
my_email varchar(255),
retype_email varchar(255),
education varchar(255),
from_ varchar(255),
in_ varchar(255),

My_Expected_compensation varchar(255),
Your_Linkedin_Profile varchar(255),
Im_a varchar(255),
My_expertise_lies_in varchar(255),
My_Core_competencies varchar(255),

My_Work_Experience varchar(255),
My_Mobile_number varchar(255),
My_Current_Employer varchar(255),
Im_available_in varchar(255)
  

);



CREATE TABLE user_credential(
  
  my_email varchar(255), 
  password varchar(255)

);

CREATE TABLE company_details(

Company varchar(255),
Investor varchar(255),
Stage varchar(255),
Type varchar(255)

);


mysql --local-infile=1 -u root -p

LOAD DATA LOCAL INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\company_details.csv' 
INTO TABLE company_details
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


SELECT `VARIABLE_VALUE`FROM `performance_schema`.`global_variables` WHERE `VARIABLE_NAME` = 'C:/Techcovery/project/v8/data';

INSERT INTO 
	company_details(Company, Investor, Stage, Type )
VALUES

  (ACCELDATA,Lightspeed Venture,Series A,AI),
  (APNA,,,),
  (BYJU’S,Lightspeed Venture,PE,Edutech),  
  (DARWINBOX,,Series C,Information Technology & Services),
  (DUKAAN,,Seed,E-commerce/Ecommerce),
  (FOXY,,Series A,E-commerce/Ecommerce),
  (FREIGHT TIGER,,Series A,Logistic Tech),
  (FRESHMENU,,,),
  (FRONTROW,,Seed,Edutech),
  (INDIAN ENERGY EXCHANGE,,,),
  (INNOVACCER,,Series D,Healthcare),
  (ITZCASH CARD,,,Fintech),
  (LIMEROAD,,,),
  (MAGICPIN,,Series D,Internet),
  (NEUU STORE,,Seed,Fintech),
  (OKCREDIT,,Series B,Internet),
  (ONE ASSIST,,Series C,Fintech),
  (OYO ROOMS,,,E-commerce/Ecommerce),
  (PEPPER CONTENT,,Series A,Information Technology & Services),
  (PROPERTY SHARE,,Series A,E-commerce/Ecommerce),
  (REDCARPET,,,Fintech),
  (SETU,,Series A,Fintech),
  (SHARECHAT,,,Internet),
  (SHUTTL,,Series C,Information Technology & Services),
  (TEACHMINT,,Seed,Edutech),
  (UDAAN,,Series D,Internet),
  (UNI,,Seed,Fintech),
  (YELLOW MESSENGER,,Series B,AI),
  (ZETWERK,,Series D,Information Technology & Services),
  (ZOLVE,,Seed,Fintech),
  (Ask Nicely,,Series A,Computer Software),
  (Biz2credit,,Series B,Fintech),
  (blueshift,,Series C,Internet),
  (circleoflife,,,Telco),
  (craftsvilla,,Series C,Internet);