import os
import mysql.connector
import queries
import logging
import time




from flask_mail import Mail, Message
from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
from data import message

app = Flask(__name__)
mail= Mail(app)
load_dotenv()

logging.basicConfig(
  filename = 'logging.log',
  filemode= 'a',
  format = '%(asctime)s %(levelname)s:%(message)s',
  datefmt = '%Y-%m-%d %H:%M:%S %p',
  level=logging.INFO
)

host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

mydb = mysql.connector.connect(
  host = host,
  user = user,
  password = password,
  database = database
)


mail_server = os.getenv("MAIL_SERVER")
mail_port = os.getenv("MAIL_PORT")
mail_username = os.getenv("MAIL_USERNAME")
mail_password = os.getenv("MAIL_PASSWORD")

mail_use_ssl = os.getenv("MAIL_USE_SSL")

app.config['MAIL_SERVER']= mail_server
app.config['MAIL_PORT'] = mail_port
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = mail_use_ssl
mail = Mail(app)





@app.route('/create_user/<name>,<Your_desired_start_up>,<my_email>,<retype_email>,<password>,<education>,<from_>,<in_>,<My_Expected_compensation>,<Your_Linkedin_Profile>,<Im_a>,<My_expertise_lies_in>,<My_Core_competencies>,<My_Work_Experience>,<My_Mobile_number>,<My_Current_Employer>,<Im_available_in>', methods=['GET', 'POST'])
def create_user(name, Your_desired_start_up, my_email, retype_email, password, education, from_, in_, My_Expected_compensation, Your_Linkedin_Profile, Im_a,My_expertise_lies_in, My_Core_competencies, My_Work_Experience, My_Mobile_number, My_Current_Employer, Im_available_in):

   

  start = time.time()
  logging.info("Create function start at %ss", start)

 

  

  if request.method == 'POST':
    name = request.form['name']
    Your_desired_start_up = request.form['Your_desired_start_up']
    my_email = request.form['my_email']
    retype_email = request.form['retype_email']
    password = request.form['password']
    education = request.form['education']
    from_ = request.form['from_']
    in_ = request.form['in_']
    My_Expected_compensation = request.form['My_Expected_compensation']
    Your_Linkedin_Profile = request.form['Your_Linkedin_Profile']
    Im_a = request.form['Im_a']
    My_expertise_lies_in = request.form['My_expertise_lies_in']
    My_Core_competencies = request.form['My_Core_competencies']
    My_Work_Experience = request.form['My_Work_Experience']
    My_Mobile_number = request.form['My_Mobile_number']
    My_Current_Employer = request.form['My_Current_Employer']
    Im_available_in = request.form['Im_available_in']

    mycursor = mydb.cursor()
    sql = queries.CREATE_USER
    val = (name, Your_desired_start_up, my_email, retype_email, education, from_, in_, My_Expected_compensation, Your_Linkedin_Profile, Im_a,My_expertise_lies_in, My_Core_competencies, My_Work_Experience,My_Mobile_number, My_Current_Employer, Im_available_in)
    mycursor.execute(sql, val)
    mydb.commit()

    mycursor = mydb.cursor()
    sql = queries.USER_CREDENTIAL
    val = (my_email, password)
    mycursor.execute(sql, val)
    mydb.commit()
    

        
    end = time.time()
    logging.info("Create function end at %ss", end)
    total = (end - start)
    logging.info("Create function take %ss", total)

    return redirect(url_for('signupMail',work_experience = My_Work_Experience, education = education, from_ = from_, in_ = in_ ))
    

@app.route('/signupMail/<work_experience>,<education>,<from_>,<in_>')
def signupMail(work_experience, education, from_, in_):
   
   msg = Message(message.SUBJECT, sender = message.SENDER, recipients = [message.RECIPIENT])
   #msg.body = message.MESSAGE_BODY
   #msg.html = message.MESSAGE_HTML 
   msg.html = render_template('messageHTML.html', work_experience = work_experience, education = education, from_ = from_, in_ = in_)
   mail.send(msg)
   
   return "Sent"




 

  
    

if __name__ == "__main__":

    app.run(debug=True)