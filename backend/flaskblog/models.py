from flaskblog import db
from flask import jsonify

class Submission(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	public_id=db.Column(db.String(80),nullable=False)
	email=db.Column(db.String(25),nullable=False)
	feedback=db.Column(db.Text())


	# return feedbacks
	def listFeedbacks(self):
		return jsonify({self.email,self.feedback})


	def __str__(self):
		return (self.email,self.feedback)








