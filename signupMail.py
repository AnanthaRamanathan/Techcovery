from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'arn.ananthan1998@gmail.com'
app.config['MAIL_PASSWORD'] = 'arn@sti16cs008'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route("/")
def index():
   msg = Message('Signup Successfully', sender = 'arn.ananthan1998@gmail.com', recipients = ['ananthan.arn@gmail.com'])
   msg.body = "You signup successfully"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(host="localhost", port=5005, debug=True)