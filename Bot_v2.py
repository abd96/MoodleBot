import urllib.request
import base64
import json as js
import requests
from bs4 import BeautifulSoup as bs
import os 

from requests import session
# Hello Torben
#source url = https://sso.itmc.tu-dortmund.de/openam/UI/Login?goto=http://moodle.tu-dortmund.de/login
#target url = https://moodle.tu-dortmund.de/my/ 

def raw_html_to_links(response):
	links_list= []
	soup = bs(response.text,'html.parser')
	tags = soup.findAll('a')
	for tag in tags:
		temp_url = str(tag.get('href'))
		if temp_url not in links_list  and temp_url[len(temp_url)-17:-13] == 'view' and temp_url != '#myoverview_courses_view': 
				links_list.append(temp_url)
	download_from_link(links_list[1])
	
	



def raw_html_to_PDFlinks(link):
	links_list = []
	response = requests.get(link)
	soup = bs(response.text,'html.parser')
	pdf_tags = soup.findAll('a')
	
	for tag in pdf_tags:
		temp_url= str(tag.get('href'))
	print("List of Links on the website has been succefully found !")
	

def download_from_link(link):
	login_data = {'encoded':'true',
			'goto' : 'aHR0cDovL21vb2RsZS50dS1kb3J0bXVuZC5kZS9sb2dpbg==',
			'0':	'UTF-8',
			'1':	'UTF-8',
			'IDToken1' : 'smadchri' , 
			'IDToken2' : 'euzdrva7'}
	url = link
	with requests.Session() as session: 
		post = session.post
	response = requests.get(url , data = login_data)
	soup = bs(response.text, 'html.parser')
	pdf_tags = soup.findAll('a')
	links_list = []
	for tag in pdf_tags:
		temp_url= str(tag.get('href'))
		
		if(temp_url[len(temp_url)-24:-18] == 'course' and temp_url not in links_list):
			links_list.append(temp_url)	

	



			



def doIt():
	source_url = 'https://sso.itmc.tu-dortmund.de/openam/UI/Login?goto=http://moodle.tu-dortmund.de/login'
	target_url = 'https://moodle.tu-dortmund.de/my/'

	login_data = {'encoded':'true',
			'goto' : 'aHR0cDovL21vb2RsZS50dS1kb3J0bXVuZC5kZS9sb2dpbg==',
			'0':	'UTF-8',
			'1':	'UTF-8',
			'IDToken1' : 'smadchri' , 
			'IDToken2' : 'euzdrva7'}
	links_list = []
	with requests.Session() as session:
		post = session.post(source_url ,data = login_data)
		response = session.get(target_url)

		soup = bs(response.text,'html.parser')
		tags = soup.findAll('a')
		
		for tag in tags:
			temp_url = str(tag.get('href'))
			if temp_url not in links_list  and temp_url[len(temp_url)-17:-13] == 'view' and temp_url != '#myoverview_courses_view': 
				links_list.append(temp_url)
		#post2 = session.post(tagret_url , data = login_data)
	response2 = session.get(links_list[1])	
	print(response2.text)

	


doIt()




