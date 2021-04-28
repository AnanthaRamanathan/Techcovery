import os
import logging


from flask_mail import Mail, Message
from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)


logging.basicConfig(
  filename = 'logging.log',
  filemode= 'a',
  format = '%(asctime)s %(levelname)s:%(message)s',
  datefmt = '%Y-%m-%d %H:%M:%S %p',
  level=logging.INFO
)


@app.route('/emailAccept')
def emailAccept():
  return("Accept")

@app.route('/emailDecline')
def emailDecline():
  return("Decline")




if __name__ == "__main__":

    app.run(host="localhost", port=5005, debug=True)