import requests
from bs4 import BeautifulSoup as bs

from Handlers.Handler import Handler



class ResponseHandler(Handler):

	
	def __init__(self, response, session, loginScreen):
		self.response = response
		self.session  = session
		self.loginScreen = loginScreen
		self.courses = []

	def isCourse(self, link):
		return '/course' in link and "id=" in link

	def getCourses(self):
		
		self.handling = True
		# Parse the response text
		soup = bs(self.response.text, 'html.parser')
		tags = soup.findAll('a')
		# extract all links that are course links from website
		for tag in tags:
			link = str(tag.get("href"))
			if link not in self.courses and self.isCourse(link) and not link == '#myoverview_courses_view': 
				self.courses.append(link)

		self.handling = False
		return self.courses