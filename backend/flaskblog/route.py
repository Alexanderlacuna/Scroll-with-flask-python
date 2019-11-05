

from flaskblog import app,db
from flask import jsonify,request


from flaskblog.models import Submission
import uuid
from flaskblog.utils import  send_mail
from flaskblog import mail
from flask_mail import Message




@app.route("/home")
def home():
	return "this is the home page",200

# post route for recieving

#configure web cors

#use flaskmail to send mail to client

#store the mails

@app.route("/api/submitForm",methods=['POST'])
def submitForm():

	
	try:
		data=request.get_json()
		feedback=data.get("feedback")
		email=data.get("email")
		ud=str(uuid.uuid4())
		new_feedback=Submission(public_id=ud,email=email,feedback=feedback)

		db.session.add(new_feedback)
		db.session.commit()
		send_mail("email",email)


		
	except Exception as e:
		return jsonify({
			"error":str(e)
			}),401
		



		

	# print(data.get('data'))
	# print(data.get("data"))

	
	# print(request.json)

	
	
	# print(data.email)
	# print(data.get("email"))



	return jsonify({
		"msg":"Your feedback was successfully received"
		
		})


@app.route("/api/sendMail")
def sendMail():

	try:
		send_mail("alexanderkabua@gmail.com","alexandramunene@gmail.com")

	
		
	except Exception as e:
		return str(e)
	

	return "test"





	# try:
	# 	send_mail("alexanderkabua@gmail.com","alexanderkabua@gmail.com")
		
	# except Exception as e:
	# 	return str(e)
	
	# return "hello"

