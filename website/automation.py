import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from .models import User

def extract_news(url):
	cnt = ''
	cnt += ('<b>HN Top News Stories:</b>\n' + '<br>' + '-'*50 + '<br>')
	response = requests.get(url)
	content = response.content
	soup = BeautifulSoup(content, 'html.parser')
	for i, tag in enumerate(soup.find_all('td', attrs = {'class': 'title', 'valign': ''})):
		cnt+= ((str(i+1)+'::'+tag.text+'\n'+'<br>')if tag.text!='More' else '')
	
	return (cnt)

def send_email(content, now, TO):
	cnt = extract_news('https://news.ycombinator.com/')
	content += cnt
	content += ('<br>-----------<br>')
	content += ('<br><br> End of Message')
	
	SERVER='smtp.gmail.com'
	PORT=587
	FROM='gauravtripathi725@gmail.com'
	# TO= ['tripathi.rksaurav@gmail.com','gauravtripathii7979@gmail.com']
	PASS='gauravtripathii'
	
	msg = MIMEMultipart()
	msg['SUBJECT'] = 'Top Stories  ' + str(now.day) + str(now.year)
	msg['FROM']=FROM
	msg['TO']=','.join(TO)
	
	msg.attach(MIMEText(content, 'html'))
	
	#--main--
	
	server = smtplib.SMTP(SERVER, PORT)
	server.ehlo()
	server.starttls()
	server.login(FROM, PASS)
	server.sendmail(FROM, TO, msg.as_string())
	server.quit()