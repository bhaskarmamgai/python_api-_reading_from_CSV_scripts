import requests
import json
import urllib.parse
from itertools import chain


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pandas.io.json import json_normalize

# lat='8.115674'
# lon='77.456099'

fa=open('lat1.txt',"r")
fb=open('lon1.txt',"r")

list1=fa.read()
format_list1=list1.strip('[,]')
# print(format_list1)
print(type(format_list1))

formatted_split_list1=format_list1.split(",")
print(type(formatted_split_list1))
print(len(formatted_split_list1))

list2=fb.read()
format_list2=list2.strip('[,]')
# print(format_list2)
print(type(format_list2))

formatted_split_list2=format_list2.split(",")
print(type(formatted_split_list2))
print(len(formatted_split_list2))

c = 0;

for a,b in zip(formatted_split_list1,formatted_split_list2):
	try:
		#print(a,b)
		#URL http://api.open-notify.org/iss-pass.json?lat={}&lon={}
		api_url="http://maps.googleapis.com/maps/api/geocode/json?latlng={},{}8&sensor=false".format(a,b)
		# api_url="http://api.open-notify.org/iss-pass.json?lat={}&lon={}".format(a,b)

		data = requests.get(api_url)
		json_data = data.json()
		# print(json_data['status'])
		# print(type(json_data))
		# print(json_data)
		# break
		if json_data['status']=='OK':
			print(type(json_data))
			#print(json_normalize(json_data))
			formatted_address = json_data['results'][0]['formatted_address']
			print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"%(a,b,formatted_address))
			
		else:
			print(json_data)
			print("\nStatus Not Okay")
			print("Error Occur at lat :{}".format(a))
			print("Error Occur at lan :{}".format(b))			
			c = c + 1;
		
		#Writting response in a file
		# f= open("data.txt","w+")
		# f.write(str(json_data))
		# f.close()
		# break

		#Normal Dictionary key vale indexing
		#print(json_data["results"]["address_components"])

	except Exception as e:
		print("Error-------Inside------------Ecxcept-----------")
		print(e)
		# print("Error Occur at lat :{}".format(a))
		# print("Error Occur at lan :{}".format(b))
		
print(c)