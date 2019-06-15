import requests
from bs4 import BeautifulSoup as bs

from Handlers.Handler import Handler


class LoginHandler(Handler):
	
	def __init__(self,username, password, loginScreen):
		super()
		self.login_source_url = 'https://sso.itmc.tu-dortmund.de/openam/UI/Login?goto=http://moodle.tu-dortmund.de/login'
		self.login_target_url = 'https://moodle.tu-dortmund.de/my/'
		self.login_data= {
				'goto' : 'aHR0cDovL21vb2RsZS50dS1kb3J0bXVuZC5kZS9sb2dpbg==',
				'0':	'UTF-8',
				'1':	'UTF-8',
				'IDToken1' : username  , 
				'IDToken2' : password 
		}
		self.loginScreen = loginScreen
	
	# @return (response, session)
	def login(self):
		
		self.handling = True
		with requests.Session() as session :
			post = session.post(self.login_source_url , data = self.login_data)
			response = session.get(self.login_target_url)
		
		# status code not 200 ?? WTF?
		if response.status_code != 200:
			self.loginScreen.notify(f"Error when logging in to moodle with status code {response.status_code}")

		# check title 
		soup = bs(response.text, 'html.parser')
		# Convension : in this case there is only one element with title tag
		t = soup.findAll('title')
		title = str(t[0])
		
		self.handling = False

		# unvalid username or password
		if ('(GUEST)'in title):
			self.loginScreen.notify("Unvalid Username or password, why wont you try again!")
			
			return None, None
		# valid username or password
		else:
			self.loginScreen.notify("Login Successfully")
			return response, session

