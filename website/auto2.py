import time
import webbrowser

while True:
	webbrowser.open('http://127.0.0.1:5000/send_all')
	time.sleep(60*60*24)