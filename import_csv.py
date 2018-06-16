import pandas
#col of CSV excel sheet
colnames = ['id', 'lat', 'lon', 'city', 'state']
#CSV file name mmf_fs.csv
data = pandas.read_csv('mmf_fs.csv',header=0)

#Col items needed in list here id,lat and lon columns are extracted intolist
id = data.id.tolist()
lat = data.lat.tolist()
lon = data.lon.tolist()

#To check Consistency in CSV columns
#Check lenght of each col and they must be equal 
a = len(id)
b = len(lat)
c = len(lon)
print(a,b,c)

try:
	if (a == b == c):
		print ("consitent CSV")
	else:
		print ("inconsitent CSV")
except:
	print ("ERROR OCUUR WHILE PARSING")


# print(id)
# print("******************")
# print(lat)
print("********LONGITUDES and LATITUDES**********")
print("\n Total Entries:")
# print(len(lon))
# print(*lon,sep='\n')


#Writting or stoing result in .txt file
f= open("lat.txt","w+")
f.write(str(lat))
f.close()
print("Latitudes Write Success")
print("\n Total Entries:")
print(len(lon))


f= open("lon.txt","w+")
f.write(str(lon))
f.close()
print("Longitudes Write Success")
print("\n Total Entries:")
print(len(lon))




