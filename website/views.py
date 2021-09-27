from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import User
import datetime
from .automation import send_email

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home_page():
	emails = User.query.all()

	if request.method=='POST':
		email=request.form.get('email')
		email_exists=User.query.filter_by(email=email).first()
		if email_exists:
			print('email already exists!!')
		else:
			new_email = User(email=email)
			db.session.add(new_email)
			db.session.commit()

	return render_template('index.html', emails=emails)

@views.route('/abcxyz')
def abc():
	return render_template('admin.html')


@views.route('/send_all')
def send():
	emails = User.query.all()
	content = ''
	now = datetime.datetime.now()

	email_list = [E.email for E in emails]
	print(email_list)

	send_email(content, now, email_list)
	print('sent')

	return redirect(url_for('views.home_page'))