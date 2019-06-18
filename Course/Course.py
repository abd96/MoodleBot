import requests
import re
from bs4 import BeautifulSoup as bs
from kivy.uix.button import Button

class Course():
	
	def __init__(self, session, courseLink):
		self.session = session
		self.courseLink = courseLink
		self.response = self.open_courseLink()
		self.soup = bs(self.response.text, 'html.parser')
		self.title = self.get_title()
		## Button ## 
		self.btn = Button(text=f'{self.title}', size_hint_y=(.15,.09), height=44,
                         on_release=lambda btn: print(btn.text))
		self.btn.size_hint_y = None
		self.btn.height = 44 

	def get_btn(self):
		return self.btn

	def open_courseLink(self):
		response = self.session.get(self.courseLink)
		return response
	
	def title(self):
		if self.title: return self.title
		else: return self.get_title

	def get_title(self):
		title = self.soup.findAll('title')
		title = re.sub('<title>' ,'',str(title))	
		title = re.sub('</title>','' , str(title))
		return title