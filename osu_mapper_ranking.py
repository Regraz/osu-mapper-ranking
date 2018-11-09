import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import re


mapset_iterator=1



class beatmap_creator:
	__mapsetowner_name=[]
	__mapsetowner_id=0
	def __init__(self, mapper, mapperid):
		self.__mapsetowner_name.insert(0,mapper)
		self.__mapsetowner_id=mapperid
	def add_name(self,another_name):
		self.__mapsetowner_name.append(another_name)
	def show_all_names(self):
		print (self.__mapsetowner_name)

class beatmap:
		


html_resp=urllib.request.urlopen('https://osu.ppy.sh')
html_download=html_resp.read()
html_breakdown=BeautifulSoup(html_download)


