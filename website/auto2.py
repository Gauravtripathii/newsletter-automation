import requests
import time

BASE='http://127.0.0.1:5000/'

while True:
	response=requests.get(BASE+'all-emails')
	print('email sent!')
	time.sleep(60*60*24)