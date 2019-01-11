import requests,json,sys,re,os
from datetime import datetime


from VideoIDHelper import *

#if you intend to extend this module
#simply call
#saveYouTubeAnnotations.retrieveAnnotation
#
#arg is either an ID, link or shortened link
#and location is the location the XML file is to be saved in
def retrieveAnnotation(arg,location="annotationXMLs/"):
	#print(idExtractor(arg))
	contents = b""
	try:
		vID = idExtractor(arg)
		pars = {"video_id" : vID}
		r = requests.get("https://www.youtube.com/annotations_invideo", params=pars)
		contents = r.content
		if(len(contents) != 0):
			try:
				with open( (location+"/{}.xml").format(vID),"wb") as f:
					f.write(contents)
			except:
				with open( (location+"{}.xml").format(vID),"wb") as f:
					f.write(contents)
		else:
			return None
		return contents
	except:
		return None
	return None

def main():
	first = True
	argument = ""
	print( "Hello today is: " + str(datetime.now().month) + "/" + str(datetime.now().day))
	print( "Remember that we have time until: " + "1/15" + " (presumably PST 0:00) " )
	while first or argument == "":
		#argument ="horse"
		argument = input("Type in a URL to video or its ID: ")
		try:
			if argument == "":
				print("Program Terminated")
				break
			result = retrieveAnnotation(argument)
			if result != None:
				print("Loaded Succesfully.")
			else:
				print("Unable to Load, File not Generated.")
		except:
			print("Unable to recognize {}".format(argument))
			print("Program Terminated")
			break
		#argument = ""
		#first = False


if __name__== "__main__":
	main()