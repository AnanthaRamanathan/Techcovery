import os
import mysql.connector
import queries
import logging
import time

from flask import Flask, request, render_template
from dotenv import load_dotenv

app = Flask(__name__)
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

@app.route('/', methods=('GET', 'POST'))
def recruterSignUpPage():
   return render_template('recruterSignUp.html')

@app.route('/recruterSignUpDetails/<CompanyName>,<ContactPerson>,<OfficialEmailID>,<Password>,<SlackID>,<ContactNumber>', methods=('GET', 'POST'))
def recruterSignUpDetails(CompanyName, ContactPerson, OfficialEmailID, Password, SlackID, ContactNumber):

    start = time.time()
    logging.info("recruterSignUpDetails function start at %ss", start)

    if request.method == 'POST':

        CompanyName = request.form['CompanyName']
        ContactPerson = request.form['ContactPerson']
        OfficialEmailID = request.form['OfficialEmailID']
        Password = request.form['Password']
        SlackID = request.form['SlackID']
        ContactNumber = request.form['ContactNumber']


        print(CompanyName)

        mycursor = mydb.cursor()
        sql = queries.RECRUTER_SIGNUP_DETAILS
        val = (CompanyName, ContactPerson, OfficialEmailID, SlackID, ContactNumber)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor = mydb.cursor()
        sql = queries.RECRUITER_CREDENTIAL
        val = (OfficialEmailID, Password)
        mycursor.execute(sql, val)
        mydb.commit()
        
        end = time.time()
        logging.info("recruterSignUpDetails function end at %ss", end)
        total = (end - start)
        logging.info("recruterSignUpDetails function take %ss", total)

        
        return render_template('loginRecruter.html')
        
        



if __name__ == "__main__":

    app.run(host="localhost", port=5010, debug=True)