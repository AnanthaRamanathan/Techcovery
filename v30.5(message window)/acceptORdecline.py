import os


from flask_mail import Mail, Message
from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
from data import message

app = Flask(__name__)
mail= Mail(app)
load_dotenv()

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







@app.route('/slackChat')
def slackChat():
  return("slack Chat")


@app.route('/jobDescription')
def jobDescription():
  return("job description")
  



  

@app.route('/jobOpening')
def jobOpening(): 
  return("job Opening")




if __name__ == "__main__":

    app.run(host="localhost", port=5005, debug=True)