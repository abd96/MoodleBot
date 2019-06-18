import requests
import re
from bs4 import BeautifulSoup as bs

from Handlers.Handler import Handler
from Course.Course import Course

class CourseHandler(Handler):

	def __init__(self, session, loginScreen, courseLinks):
		self.session = session 
		self.courseLinks = courseLinks # list of links to found courses
		self.loginScreen = loginScreen

	def handle(self):

		for courseLink in self.courseLinks:
			# Every object of course will automaticlly open the given link and save the 
			# reponse as private attribute
			course = Course(self.session, courseLink)
			
			self.loginScreen.addToDropdown(course.get_btn())
					
		self.loginScreen.show_dropdown()
		self.loginScreen.notify("Select course to download")