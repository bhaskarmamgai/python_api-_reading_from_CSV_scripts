import requests
import json
import urllib.parse
from itertools import chain


from urllib.request import urlopen
from bs4 import BeautifulSoup

# lat='8.115674'
# lon='77.456099'

#Opening .txt file in read mode although its looks like a list but its a string as whole
fa=open('lat.txt',"r")
fb=open('lon.txt',"r")

#On split()extra op ['[1,1,..]']
# lines = fa.read().split() without split normal list as []
list1 = fa.read()

#print(lines)
print(len(list1.split()))


list2 = fb.read()
n= len(list2.split())
print(n)
print("Open succces")

# lat='8.115674'
# lon='77.456099'
# address = "1hr"
# api_url="http://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&sensor=false".format(lat,lon)
# url = api_url + urllib.parse.urlencode({'address':address})
# json_data = requests.get(url).json()
# print(json_data)



#Testing URL Static
lat = 40.71 
lon= -74
api_url="http://api.open-notify.org/iss-pass.json?lat={}&lon={}".format(lat,lon)
json_data = requests.get(api_url).json()
print(json_data)
print(json_data["request"]["datetime"])




# for (a, b) in zip(list1, list2):
# 	try:
# 		print(a , b)
# 		#print(lines)
# 		#address = "1hr"
# 		#key value pair
# 		api_url="http://api.open-notify.org/iss-pass.json?lat={}&lon={}".format(list1,list2)

# 		#url = api_url + urllib.parse.urlencode()
# 		json_data = requests.get(api_url).json()

# 		print(json_data)
# 	except:
# 		print("ERROR")


#float_list = float(list1)
#print(float_list)
#print(float_list)



#Converting list string into list of string using split function seprated by "'"
#Remember [] is either removed from txt voluntary to make first elementslist[0] from "[" and "]" from last list[n]
formated_list1 = list1.split(",")
print((formated_list1[0]))

formated_list2 = list2.split(",")
print((formated_list2[0]))

for a,b in zip(formated_list1,formated_list2):
	try:
		#print(a,b)
		#URL http://api.open-notify.org/iss-pass.json?lat={}&lon={}
		api_url="http://api.open-notify.org/iss-pass.json?lat={}&lon={}".format(a,b)
		json_data = requests.get(api_url).json()
		#print(json_data)
		#Normal Dictionary key vale indexing
		print(json_data["request"]["datetime"])
	except:
		print("Error Occur")

print(len(formated_list1))
print(len(formated_list2))

	



	


