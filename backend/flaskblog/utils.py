 # function for dealing with mail
from flask_mail import Message
from flaskblog import mail
def send_mail(sender,receivers):
	msg=Message('Hello',sender="alexanderkabua@gmail.com",recipients=[receivers])
	link="http://localhost:5000"
	msg.body=f"A feedback has been received   from {receivers}  to view visit {link}"
	mail.send(msg)


