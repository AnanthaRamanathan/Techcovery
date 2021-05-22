import os
import mysql.connector
import queries
import logging
import time

from flask_mail import Mail, Message
from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
from data import message

from flask import Flask, request, render_template
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
mail= Mail(app)

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

@app.route('/', methods=('GET', 'POST'))
def recruterSignUpPage():
   return render_template('recruterSignUp.html')

@app.route('/recruterSignUpDetails/<CompanyName>,<ContactPerson>,<OfficialEmailID>,<hashEmail>,<Password>,<SlackID>,<ContactNumber>', methods=('GET', 'POST'))
def recruterSignUpDetails(CompanyName, ContactPerson, OfficialEmailID, hashEmail, Password, SlackID, ContactNumber):

    start = time.time()
    logging.info("recruterSignUpDetails function start at %ss", start)

    if request.method == 'POST':

        CompanyName = request.form['CompanyName']
        ContactPerson = request.form['ContactPerson']
        OfficialEmailID = request.form['OfficialEmailID']
        
        Password = request.form['Password']
        SlackID = request.form['SlackID']
        ContactNumber = request.form['ContactNumber']

        hashEmail = hash(OfficialEmailID)
        verification = "No"
        print(CompanyName)
        print(hashEmail)

        mycursor = mydb.cursor()
        sql = queries.RECRUTER_SIGNUP_DETAILS
        val = (CompanyName, ContactPerson, OfficialEmailID, SlackID, ContactNumber)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor = mydb.cursor()
        sql = queries.RECRUITER_CREDENTIAL
        val = (OfficialEmailID, Password, verification, hashEmail)
        mycursor.execute(sql, val)
        mydb.commit()
        
        end = time.time()
        logging.info("recruterSignUpDetails function end at %ss", end)
        total = (end - start)
        logging.info("recruterSignUpDetails function take %ss", total)


        msg = Message(message.VERIFY_MAIL_SUBJECT, sender = message.SENDER, recipients = [message.RECIPIENT]) 
        msg.html = render_template('verifyEmail.html',hashEmail = hashEmail)
        mail.send(msg)

        
        return render_template('signupsuccessfully.html')
        
        



if __name__ == "__main__":

    app.run(host="localhost", port=5010, debug=True)