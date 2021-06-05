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

@app.route('/emailConfirm/<hashEmail>', methods=('GET', 'POST'))
def emailConfirm(hashEmail):
    print(hashEmail)

    mycursor = mydb.cursor()
    sql = queries.VERIFY_MAIL
    val = (hashEmail, )
    mycursor.execute(sql, val)
    mydb.commit()

    mycursor = mydb.cursor()
    sql = queries.CANDIDATE_RECRUITER
    val = (hashEmail, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    print(myresult)

    candidate=[('candidate',)]
    recruiter=[('recruiter',)]

    if (myresult == candidate):
      return render_template('loginCandidate.html')
    elif (myresult == recruiter):
      return render_template('loginRecruter.html')
    else:
      return "Invalid user"
        



if __name__ == "__main__":

    app.run(host="localhost", port=5012, debug=True)