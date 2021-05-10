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






@app.route('/create_user/<name>,<type_>,<stage>,<company>,<my_email>,<retype_email>,<password>,<education>,<from_>,<in_>,<CandidateStatus>,<CandidateStatusActive>,<My_Expected_compensation>,<Your_Linkedin_Profile>,<Your_Linkedin_ProfileActive>,<Im_a>,<My_expertise_lies_in>,<My_Core_competencies>,<My_Core_competenciesActive>,<My_Work_Experience>,<My_Mobile_number>,<My_Current_Employer>,<Im_available_in>', methods=['GET', 'POST'])
def create_user(name, type_, stage, company, my_email, retype_email, password, education, from_, in_, CandidateStatus, CandidateStatusActive, My_Expected_compensation, Your_Linkedin_Profile, Your_Linkedin_ProfileActive, Im_a,My_expertise_lies_in, My_Core_competencies, My_Core_competenciesActive, My_Work_Experience, My_Mobile_number, My_Current_Employer, Im_available_in):

   

  start = time.time()
  logging.info("Create function start at %ss", start)

 

  

  if request.method == 'POST':
    
    name = request.form['name']
    


    type_ = request.form['type_']
    stage = request.form['stage']
    company = request.form['company']



    my_email = request.form['my_email']
    retype_email = request.form['retype_email']
    password = request.form['password']
    education = request.form['education']
    from_ = request.form['from_']
    in_ = request.form['in_']

    CandidateStatus = request.form['CandidateStatus']
    CandidateStatusActive = request.form['CandidateStatusActive']

    My_Expected_compensation = request.form['My_Expected_compensation']

    Your_Linkedin_Profile = request.form['Your_Linkedin_Profile'] or request.form['Your_Linkedin_ProfileActive']

    Im_a = request.form['Im_a']
    My_expertise_lies_in = request.form['My_expertise_lies_in']

    My_Core_competencies = request.form['My_Core_competencies'] or request.form['My_Core_competenciesActive'] 


    My_Work_Experience = request.form['My_Work_Experience']
    My_Mobile_number = request.form['My_Mobile_number']
    My_Current_Employer = request.form['My_Current_Employer']
    Im_available_in = request.form['Im_available_in']

    mycursor = mydb.cursor()
    sql = queries.CREATE_USER
    val = (name, type_, stage, company, my_email, retype_email, education, from_, in_, CandidateStatus, CandidateStatusActive, My_Expected_compensation, Your_Linkedin_Profile, Im_a,My_expertise_lies_in, My_Core_competencies, My_Work_Experience,My_Mobile_number, My_Current_Employer, Im_available_in)
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

    
    

    usrDetails (name, type_, stage, company, my_email, retype_email, education, from_, in_,CandidateStatus, CandidateStatusActive, My_Expected_compensation, Your_Linkedin_Profile, Im_a,My_expertise_lies_in, My_Core_competencies, My_Work_Experience,My_Mobile_number, My_Current_Employer, Im_available_in)

  return redirect(url_for('signupMail',work_experience = My_Work_Experience, education = education, from_ = from_, in_ = in_, name = name, company = company, Your_Linkedin_Profile=Your_Linkedin_Profile))


def usrDetails (name, type_, stage, company, my_email, retype_email, education, from_, in_,CandidateStatus, CandidateStatusActive, My_Expected_compensation, Your_Linkedin_Profile, Im_a,My_expertise_lies_in, My_Core_competencies, My_Work_Experience,My_Mobile_number, My_Current_Employer, Im_available_in):
  global name1, type_1, stage1, company1, my_email1, retype_email1, education1, from_1, in_1,CandidateStatus1, CandidateStatusActive1, My_Expected_compensation1, Your_Linkedin_Profile1, Im_a1, My_expertise_lies_in1, My_Core_competencies1, My_Work_Experience1, My_Mobile_number1, My_Current_Employer1, Im_available_in1
  name1 = name
  type_1 = type_
  stage1 = stage
  company1 = company
  my_email1 = my_email
  retype_email1 = retype_email
  education1 = education
  from_1 = from_
  in_1 = in_
  CandidateStatus1 = CandidateStatus
  CandidateStatusActive1 = CandidateStatusActive
  My_Expected_compensation1 = My_Expected_compensation
  Your_Linkedin_Profile1 = Your_Linkedin_Profile
  Im_a1 = Im_a
  My_expertise_lies_in1 = My_expertise_lies_in
  My_Core_competencies1 = My_Core_competencies
  My_Work_Experience1 = My_Work_Experience
  My_Mobile_number1 = My_Mobile_number
  My_Current_Employer1 = My_Current_Employer
  Im_available_in1 = Im_available_in

@app.route('/signupMail/<work_experience>,<education>,<from_>,<in_>,<name>,<company>')
def signupMail(work_experience, education, from_, in_, name, company):
   
   linkedin = request.args.get('Your_Linkedin_Profile')
   


   msg = Message(message.SUBJECT, sender = message.SENDER, recipients = [message.RECIPIENT])
   msg.html = render_template('recruiterMail.html', work_experience = work_experience, education = education, from_ = from_, in_ = in_, name = name, company = company, linkedin=linkedin)
   mail.send(msg)
   
   

   
   #return ("sent")
   return render_template('loginCandidate.html', name = name)


@app.route('/emailAccept', methods=['GET', 'POST'])
def emailAccept():
   
   

   
   msg = Message(message.STATUS_SUBJECT, sender = message.SENDER, recipients = [message.RECIPIENT]) 
   msg.html = render_template('candidateAcceptMail.html', name=name1, company=company1)
   mail.send(msg)
   
   
   return redirect(url_for('candidate'))
   
@app.route('/candidate')
def candidate():
  status = CandidateStatus1

  
  if (status == "active" ):
    
    
    return render_template('activeCandidate.html', name = name1, email = my_email1, phone = My_Mobile_number1, education = education1, Employment = My_Current_Employer1, Linkedin =  Your_Linkedin_Profile1, Compensation = My_Expected_compensation1, NoticePeriod = Im_available_in1,  Experience = My_Work_Experience1, CandidateStatus = CandidateStatus1, competencies = My_Core_competencies1, expertise = My_expertise_lies_in1, Current_Employer = My_Current_Employer1)

  else:
    
    return render_template('passiveCandidate.html', name = name1, email = my_email1,  education = education1, Linkedin =  Your_Linkedin_Profile1, Compensation = My_Expected_compensation1, CandidateStatus = CandidateStatus1, competencies = My_Core_competencies1)
    
    

@app.route('/emailDecline')
def emailDecline():
  msg = Message(message.STATUS_SUBJECT, sender = message.SENDER, recipients = [message.RECIPIENT]) 
  msg.html = render_template('candidateDeclineMail.html', name=name1, company=company1)
  mail.send(msg)

  return("sent DECLINE mail to candidate ")






 

  
    

if __name__ == "__main__":

    app.run(debug=True)