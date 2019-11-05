from flask import Flask,render_template
import os

from flask_cors import CORS

import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message





app=Flask(__name__)
# email configuration

app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=587
app.config["MAIL_USERNAME"]="email"
app.config["MAIL_PASSWORD"]="password"
app.config["MAIL_USE_TLS"]=True
app.config["MAIL_USE_SSL"]=False

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:////tmp/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

mail=Mail(app)

# set up the db instance
db=SQLAlchemy(app)

CORS(app)


from flaskblog.route import home,submitForm,sendMail


@app.route("/test")
def test():
	return render_template("dashboard.html")
app.config["SECRET_KEY"]=os.urandom(16)


   


