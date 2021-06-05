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

@app.route('/authenticate_user/<email>,<password>', methods=('GET', 'POST'))
def authenticate_user(email, password):

    start = time.time()
    logging.info("authenticate_user function start at %ss", start)

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email)
        print(password)


        login_cursor = mydb.cursor()
        sql = queries.LOGIN
        val = (email, password)
        login_cursor.execute(sql, val)
        role = login_cursor.fetchall()
        login_cursor.close()
        
        end = time.time()
        logging.info("authenticate_user function end at %ss", end)
        total = (end - start)
        logging.info("authenticate_user function take %ss", total)

        print(role)
        
        candidate=[('candidate',)]
        recruiter=[('recruiter',)]

        if (role == candidate):

          login_cursor = mydb.cursor()
          sql = queries.ACCEPTANCE_RECRUITER
          val = (email, )
          login_cursor.execute(sql, val)
          recruiter = login_cursor.fetchall()
          recruiter1 = recruiter[0]
          recruiter2 = recruiter1[0]
          print(recruiter2)

          mycursor = mydb.cursor()
          sql = queries.CANDIDATE_NAME
          val = (email, )
          mycursor.execute(sql, val)
          name = mycursor.fetchall()
          n = name[0]
          n1 =n[0]

          print(n[0])


          return render_template('loginCandidate.html', recruiter_company = recruiter2, name = n1, email = email)
        elif (role == recruiter):



          return render_template('loginRecruter.html', email = email)
        else:
          return "Invalid user"
        


        
if __name__ == "__main__":

    app.run(host="localhost", port=5001, debug=True)