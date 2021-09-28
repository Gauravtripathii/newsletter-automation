from website import create_app, db
from website.models import User
from website.automation import send_email
from flask_restful import Api, Resource
import datetime

app=create_app()
api=Api(app)

class SendingData(Resource):
	def get(self):
		emails = User.query.all()
		content = ''
		now = datetime.datetime.now()

		email_list = [E.email for E in emails]
		print(email_list)

		send_email(content, now, email_list)
		print('sent')

		return {'emails':[email_list]}


api.add_resource(SendingData,'/all-emails')


app.run(debug=True)