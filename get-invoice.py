#!/usr/bin/env python3

import requests
import time
import os

USERNAME=''
PASSWORD=''

START_URL= 'https://www.unitymedia.de/benutzerkonto/login/zugangsdaten/'
LOGIN_URL='https://www.unitymedia.de/auth-handler/iam/authenticateuser/'
PDF_BASE_URL='https://www.unitymedia.de/kundencenter/meine-rechnungen/alle-rechnungen.updatebillspayments.GET?action=get_pdf_bill&doc_id='
SESSION = requests.Session()


def do_login(username='',password=''):
	# start url
	SESSION.get(START_URL)

	# do login request
	login_data = {'source': 'AEM', 'target': 'AEM', 'URL': '', 'userId': username, 'password': password}
	login_req = SESSION.post(LOGIN_URL, data=login_data)
	res = login_req.text
	#print("Title is %s", title)

def get_invoice_list():
	res = SESSION.get('https://www.unitymedia.de/kundencenter/meine-rechnungen/alle-rechnungen/_jcr_content/par.ajax')
	return res.text

def download_invoice_pdf(res):
	doc_id = res.split('get_pdf_bill&doc_id=',2)[1].split('"',2)[0]
	date_string = res.split('get_pdf_bill&doc_id=',2)[1].split('<div class="myc-invoice-summary__period">',2)[1].split('</div>')[0].strip().split('-', 2)[0]
	date = time.strptime(date_string, '%a %b %d %X %Z %Y')
	filename = time.strftime('%Y-%m', date) + '.pdf'
	if os.path.isfile(filename) == False:
		res = SESSION.get(PDF_BASE_URL + doc_id)
		print("Downloading " + filename)
		open(filename, 'wb').write(res.content)
	else:
		print("No new invoice")


def init():
	global USERNAME
	global PASSWORD
	config = open('./login.txt', 'r')
	USERNAME = config.readline().strip()
	PASSWORD = config.readline().strip()

init()
print('user: ' + USERNAME)
print('password: ' + PASSWORD)
do_login(USERNAME, PASSWORD)
download_invoice_pdf(get_invoice_list())




