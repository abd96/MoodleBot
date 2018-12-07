
import urllib.request
import base64
import json as js
import requests
from bs4 import BeautifulSoup as bs
import os 

from requests import session
def main():
	print("Sending request and reciving the response from url \n")
	#@request anfordern und response speichern

	url = 'https://moodle.tu-dortmund.de/course/view.php?id=12903' 
	response = requests.get(url , auth=('StatI' , 'deskriptiv') )
	print(response.status_code)
	soup = bs(response.text,'html.parser')
	 
	links_list = []
	
	pdf_tags = soup.findAll('a')
	
	for tag in pdf_tags:
		temp_url = url + str(tag.get('href'))	
		
		
		if( temp_url.endswith('.pdf')):
			links_list.append(temp_url)
					
	print("pdf links found on the website are : \n {}".format(links_list))

	if not os.path.exists('pdfs'):
		os.makedirs('pdfs')
	os.chdir('pdfs')
	i = 0
	print(len(links_list))
	for pdf_link in links_list:
		try:
			source = requests.get(pdf_link)
			if source.status_code==200:
				print("LINK IS VALID LINK ! ")
				with open('pdf-' +str(i)+'.pdf' , 'wb') as f:
					f.write(requests.get(url).content)
					f.close()
					x+=1
		except:
			print("PASSING ")
			pass
main()

	
"""def request_it(url, username , password):
	
		response = requests.get(url , auth = (username , password))
		if(response.status_code == 401):
			print("Login required or wrong login data... please try again ! \n username ->")
			username = input()
			print("password -> ")
			passwort = input()
			request_it(url , str(username) , str(passwort))
		else:
			print("login success!")
			return response"""
	
def raw_html_to_links(response):
	links_list = []
	soup = bs(response.text,'html.parser')
	pdf_tags = soup.findAll('a')
	for tag in pdf_tags:
		temp_url = url + str(tag.get('href'))
		if(temp_url.endwith('.pdf')):
			links_list.append(temp_url)
	print("List of Links on the website has been succefully found !")	






