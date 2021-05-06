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


        mycursor = mydb.cursor()
        sql = queries.AUTHENTICATE_USER
        val = (email, password)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        
        end = time.time()
        logging.info("authenticate_user function end at %ss", end)
        total = (end - start)
        logging.info("authenticate_user function take %ss", total)

        print(myresult)
        if (len(myresult) > 0):
          return render_template('loginCandidate.html')
        else:
          return "Invalid user"
        



if __name__ == "__main__":

    app.run(host="localhost", port=5001, debug=True)