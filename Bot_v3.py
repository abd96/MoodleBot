import urllib.request 
import base64
import json as js 
from bs4 import BeautifulSoup as bs
import os 
import sys
import requests
from requests import session 
import re
import time
import datetime
import getpass

"""-------------------------------------------------------------------------------------------------------------

	/home/abdul/Schreibtisch/Python/MoodleBot/pdfs/*******
	RvS_Bot
	Logik_Bot
	******_Bot	


-------------------------------------------------------------------------------------------------------------"""

#*************************************************************************************************************

login_source_url = 'https://sso.itmc.tu-dortmund.de/openam/UI/Login?goto=http://moodle.tu-dortmund.de/login'
login_target_url = 'https://moodle.tu-dortmund.de/my/' 
pointerDict = {
	

	'[Kurs: Funktionale Programmierung WiSe 2018/19]' : 'FuPro',
	'[Kurs: Logik, LSF, 040125]' : 'Logik'	,
	'[Kurs: Datenstrukturen, Algorithmen und Programmierung 2, LSF, 040115]' : 'Dap2',
	'[Kurs: Übung zu Mathematik für Informatiker 2]' : 'Mafi2',
	'[Kurs: Softwaretechnik, LSF, 040135]' : 'Swt',
	'[Kurs: Übung Rechnernetze und verteilte Systeme, LSF, 040114]' : 'RvS',
	'[Kurs: Elektrotechnik / Nachrichtentechnik für Informatiker, 080625, 2018]' : 'Etnt'



}

#*************************************************************************************************************
# @Login to Moodle and open a session to work on 

# :Param username : Moodle Account-username 
# :Param password : Moodle Account-password
# :Param download_path : a Path to download all files to 

def logIn_2Moodle(username , download_path  ):

	# Calculate Time 
	start_time = datetime.datetime.now()
	print('<Excuted: {}>'.format(start_time))
	print('Logging into Your UniAccount please wait. . .')
	#@try to login to UniAccount using internet connection  
	try :
		# @Dictionary containing all the neccessry information about logging a user into the webpage
		# @This may vary depending on the webbrowser you are using 
		
		login_data, post, response, session = login(username)
		"""getpass.getpass("Enter your password {}: ".format(username))
		soup1 = bs(response.text, 'html.parser')
		title = soup1.findAll('title')
		if('(GUEST)' not in title):
		break

		login_data= {
				'goto' : 'aHR0cDovL21vb2RsZS50dS1kb3J0bXVuZC5kZS9sb2dpbg==',
				'0':	'UTF-8',
				'1':	'UTF-8',
				'IDToken1' : username  , 
				'IDToken2' : password 
		}
		# @We need to open a session to get a session key where we can get the links and 
		# the data in every link found in there(a sessionID is only for ca. 15-Minutes valid  ). 
		with requests.Session() as session :
			# @Sending a post-request to my session with login-information and the link
			post = session.post(login_source_url , data = login_data)
			# @Recieving the get-request from our session with the raw HTML Code from the website
			response = session.get(login_target_url)
			# @Checking if the session response was successfull or not and 
			#printing masseges depenging on the status_code :: (400 | 200) 
		
		soup1 = bs(response.text, 'html.parser')
		title = soup1.findAll('title')
		print(title)"""

		if(response.status_code  == 200):	
			print('Logged in , Welcome {}'.format(username))	
		else:
			print('Login Failed , please try again')	
		# @Getting all the Links that specifie the Modul we have on our Moodle Main Page   
		links_list = find_it_in_HTML(response , session , 'view')
		# @Printing number of found Modules
		if(len(links_list) > 0 ):	
			print('Modules-links has been successfully collected')
			print('{} Modules where found '.format(len(links_list)))
		else:
			print('Error : Either you dont have any modules in your Moodle or there has been some kind of error ')
		
		# @Iterate on all the Module links and get pdf files from them
		r_pdf_dict = {}
		for module_link in links_list:
			# @Open_url helps openning a link in the same session that we are at in that time 
			module_link_response = open_url(module_link , session)
			# @Looking for pdf files using the function find_it_in_HTML with the key='pdf'  
			pdf_dict ,title_tag = find_it_in_HTML(module_link_response , session , 'pdf')
			print('{} pdf files where found! '.format(len(pdf_dict[pointerDict[title_tag]] )))
			r_pdf_dict.update( pdf_dict )
		# @Creating Folders in the given path download_path: 
		for (module, module_pdfs) in r_pdf_dict.items(): 
			folder_name = module + '_Bot'
			path_toPass = download_path + folder_name 
			print(path_toPass)
			if(os.path.exists(path_toPass)):
				print('Directory exists , downloading files to {}'.format(folder_name))
			else:
				os.makedirs(path_toPass)
				print('Directory {} has been successfully created ! '.format(path_toPass))
			print('*******************Starting Download*******************')
			for pdf in module_pdfs: 
				print(pdf)
				download_pdf( pdf , session , module , path_toPass)
			print('*******************Download finished*******************')
		# @Show the time needed to Download !	
		print('<Finished in : {}>'.format(datetime.datetime.now() - start_time))
	#@Exception thrown from no internet connection problem will be catched here.		
	except:
		print('Login Failed ! \n Please check your internet connection.')		
	






# @Param  : respose : raw-HTML representing the modul website 
# @Param  : session : the corresponding session that we are logged into 
# @Param  : key     :   
# @return : list containing all the files found in a link 
def find_it_in_HTML(response , session , key ):

	#@We will fill our links_list depending on what we are searching in the raw_HTML_Code

	#@Create an empty list
	links_list = []

	#soup is a variable that contains the parsed html code ,where we can get specified tags from it 
	soup = bs(response.text, 'html.parser')
	tags = soup.findAll('a')

	#@When filtering the HTML-Code to pdf files 
	if(key == 'pdf'):

		#@A Dictionary that will contain the Module-name(title of the page) with all references to pdf files in it. 
		#@this will be returned in the end with the title as tupel (pdfFileDict , title_tag). 
		pdfFilesDict = {}
		#@Filtering the title from the Tag
		#For all Folders in the module-website
		
		#List for adding Folders in a ModulWebpage.
		folder_List = []

		title_tag = soup.findAll('title')
		title_tag = re.sub('<title>' ,'',str(title_tag))
		title_tag = re.sub('</title>','' , str(title_tag))
		print('Getting pdf files from {} Website'.format(pointerDict[title_tag]))
		for tag in tags:
			temp_url = str(tag.get('href'))
			if( temp_url not in folder_List  and 'folder' in temp_url and 'FuPro' == pointerDict[title_tag] ) : 
				folder_List.append(temp_url)	
				"""responseFolder = open_url(temp_url , session)
				soupFolder = bs(responseFolder.text, 'html.parser')
				tagsFolder = soupFolder.findAll('a')
				for t in tagsFolder:
					temp_url_Folder = str(t.get('href'))
					if( (temp_url_Folder not in links_list ) and ( ( ('blatt' in temp_url_Folder) or ('Blatt' in temp_url_Folder) ) or ('resource' in temp_url_Folder) or ('content' in temp_url_Folder and (temp_url_Folder != '#maincontent')) ) ):
						links_list.append(temp_url_Folder)
						pdfFilesDict.update({ pointerDict[title_tag] : links_list })"""
			# Fupro has folders on the websites that needs to be opened again ! 			
			if(pointerDict[title_tag] == 'FuPro'):
				for Folder_Link in folder_List :
					FolderResponse = open_url(Folder_Link , session)
					FolderSoup = bs(FolderResponse.text , 'html.parser')
					FolderTags = FolderSoup.findAll('a')
					for t in FolderTags:
						Folder_temp_url = str(t.get('href'))
						if( (Folder_temp_url not in links_list ) and ( ( ('blatt' in Folder_temp_url) or ('Blatt' in Folder_temp_url) ) or ('resource' in Folder_temp_url) or ('content' in Folder_temp_url and (Folder_temp_url != '#maincontent')) ) ):
							links_list.append(Folder_temp_url)
					
			if( (temp_url not in links_list ) and ( ('blatt' in temp_url ) or ('resource' in temp_url) or ('content' in temp_url and (temp_url != '#maincontent')) ) ):
				links_list.append(temp_url)
				pdfFilesDict.update({ pointerDict[title_tag] : links_list })

			"""if('folder' in temp_url and ('FuPro' == pointerDict[title_tag]) ) :
				responseFolder = open_url(temp_url , session)
				soupFolder = bs(responseFolder.text, 'html.parser')
				tagsFolder = soup.findAll('a')
				for t in tagsFolder:
					temp_url_Folder = str(t.get('href'))
					if( (temp_url_Folder not in links_list ) and ( ('blatt' in temp_url_Folder ) or ('resource' in temp_url_Folder) or ('content' in temp_url_Folder and (temp_url_Folder != '#maincontent')) ) ):
						print("----------------------------------------------------------------------------------------------------------------------{}".format(temp_url_Folder))
						links_list.append(temp_url_Folder)
						print(links_list)
						pdfFilesDict.update({ pointerDict[title_tag] : links_list })"""
		return pdfFilesDict , title_tag
	#@When filtering the HTML-Code to Module-Links 
	elif(key == 'view'):
		for tag in tags:
			#@Seperate the tag from the Modul-Url
			temp_url = str(tag.get('href'))
			#@When this link ist a valued Modul-Link  
			if temp_url not in links_list and temp_url[len(temp_url)-17:-13] == 'view' and temp_url != '#myoverview_courses_view': 
				#@Then add it to our result list 
				links_list.append(temp_url)
		#@Returning the list of links back to its caller 		
		return links_list
	#@If the key is a wrong key  -> handle !
	else:
		print('Bad function call in ->  find_it_in_HTML(response , *key*? ) ' )	
		return

def download_pdf(url , session , module_name , download_path):
	try : 
		
		r = open_url(url , session )
		#print ('downloading {}'.format(r.headers['filename']))
		print( 'Downloading {} from {} website'.format ( filter_filename (r.headers['Content-Disposition'])  , module_name)  )
			
		#save_path = '/home/abdul/Schreibtisch/Python/MoodleBot/pdfs/Test_RvS'
		completeName = os.path.join( download_path , filter_filename (r.headers['Content-Disposition']) )		
		if(not os.path.isfile(completeName)):	
			file = open( completeName , 'wb')
			file.write( r.content )
			file.close()
			print('Finished downloading !')	
		else:
			print('File already exists , File skipped!')
	except:
		print('ERROR IN LINK')


def filter_filename(toFilter): 
	toFilter = re.sub('attachment; filename=' , '' , toFilter)
	toFilter = re.sub('inline; filename=' , '' , toFilter)
	toFilter = re.sub('"' , '' , toFilter)
	return toFilter


def open_url(url  , session ):
	response = session.get(url)
	return response

def login(username):
	while(True):
		password = getpass.getpass("Enter your password {}: ".format(username))	
		login_data= {
					'goto' : 'aHR0cDovL21vb2RsZS50dS1kb3J0bXVuZC5kZS9sb2dpbg==',
					'0':	'UTF-8',
					'1':	'UTF-8',
					'IDToken1' : username  , 
					'IDToken2' : password 
			}
		with requests.Session() as session :
			# @Sending a post-request to my session with login-information and the link
			post = session.post(login_source_url , data = login_data)
			# @Recieving the get-request from our session with the raw HTML Code from the website
			response = session.get(login_target_url)
			# @Checking if the session response was successfull or not and 
			#printing masseges depenging on the status_code :: (400 | 200) 
		soup1 = bs(response.text, 'html.parser')
		title = soup1.findAll('title')
		
		if('(GUEST)' not in  title):
			print("GGWP")
			break
	
	print('returning')		 	
	return login_data, post, response, session	
		

if __name__=='__main__':
	logIn_2Moodle(sys.argv[1] , sys.argv[2] )
