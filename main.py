import threading
from application.MoodleApp import MoodleApp as application

def runApplication():
	app = application()
	app.run()

def main():
	runApplication()

if __name__ == "__main__":
	
	main()