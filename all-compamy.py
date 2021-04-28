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


@app.route('/')
def index():

    mycursor = mydb.cursor()
    sql = queries.GET_ALL_COMPANY
    mycursor.execute(sql)
    companyNames = mycursor.fetchall()
    
    

    return render_template(
        'index.html', companyNames=companyNames)


if __name__ == "__main__":

    app.run(host="localhost", port=5003, debug=True)