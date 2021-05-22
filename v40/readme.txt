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

CREATE TABLE company_detail(

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
	company_details(Company, Investor, Stage, Type)
VALUES




INSERT INTO company_detail VALUES (value1, value2, value3, ...);



ALTER TABLE user_details ADD CandidateStatusActive varchar(255);


CREATE TABLE company_signupDetails(

CompanyName varchar(255), 
ContactPerson varchar(255), 
OfficialEmailID varchar(255), 
Password varchar(255), 
SlackID varchar(255), 
ContactNumber varchar(255)


);

CREATE TABLE credential(
  
  email varchar(255), 
  password varchar(255),
  role varchar(255)

);

ALTER TABLE credential
ADD emailHash varchar(100);

ALTER TABLE credential
  DROP COLUMN passwordHash;



CREATE TABLE acceptance(
  
  candidate varchar(255), 
  recruiter varchar(255)
  
);


from slack import RTMClient
import requests
import json

from kafka import KafkaProducer

bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()

@RTMClient.run_on(event="message")
def amusebot(**payload):
    
    data = payload["data"]
    #print(data)
    web_client = payload["web_client"]
    #print(web_client)
    bot_id = data.get("bot_id", "")
    #print(bot_id)

    # If a message is not send by the bot
    if bot_id == "":
        channel_id = data["channel"]
        print(channel_id)

        bootstrap_servers = ['localhost:9092']
        topicName = 'myTopic'
        producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
        producer = KafkaProducer()

        # Extracting message send by the user on the slack
        text = data.get("text", "")
        text = text.split(">")[-1].strip()
        print(text)
       

        msg = json.dumps(text).encode('utf-8') 
        producer.send(topicName, msg)

        #ack = producer.send(topicName, b'Hello World!!!!!!!!')
        #metadata = ack.get()
        #print(metadata.topic)
        #print(metadata.partition)

                
        producer = KafkaProducer(bootstrap_servers = bootstrap_servers, retries = 5,value_serializer=lambda m: json.dumps(m).encode('ascii'))
        


        

       
        response = "my hardcode response"
        print(response)
        
        # Sending message back to slack
        web_client.chat_postMessage(channel=channel_id, text=response)

try:
    rtm_client = RTMClient(token="xoxb-1733759796176-2065419109941-MsWuhfxIW3bJs03VSFRZwIcN")
    print("Bot is up and running!")
    rtm_client.start()
except Exception as err:
    print(err)

      