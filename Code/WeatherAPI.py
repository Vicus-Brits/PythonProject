## https://developer.weatherunlocked.com/signup


import requests
from requests import Response
import xml.etree.ElementTree as ET
import pandas as pd
import sqlite3


#create data structure 
data = {'temperature_c': [],
	'temperature_f': []}

#create dataframe
df_marks = pd.DataFrame(data)
print('Original DataFrame\n------------------')
print(df_marks)


# Get API data
weather_type: str = 'current'
call_string = 'http://api.weatherunlocked.com/api/' + weather_type + '/-26.2041,28.0473?app_id=0ca7c5a3&app_key=10fb8b0062bbcaf0934cedeb7a3cd23c'
 

Response = requests.get(call_string, headers={'Accept': 'text/xml'})

print(Response.status_code)
print(Response.content)  # XML 

root = ET.fromstring(Response.text)
tree = ET.ElementTree(root)
tree.write("C:/Users/cc099293/Documents/GitHub/PythonProject/Data/file.xml")

print (tree)  # object 


root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

latitude = root.find('latitude').text
temperature_c = root.find('temperature_c').text
temperature_f = root.find('temperature_f').text
feels_like_temperature_c = root.find('feels_like_temperature_c').text
feels_like_temperature_f = root.find('feels_like_temperature_f').text

print ("latitude", latitude) 
print ("temperature_c", temperature_c) 
print ("temperature_f", temperature_f) 
print ("feels_like_temperature_c", feels_like_temperature_c) 
print ("feels_like_temperature_f", feels_like_temperature_f)
 
# update dataframe 
new_row = {'temperature_c':str(temperature_c), 'temperature_f':str(temperature_f)}
#append row to the dataframe
df_marks = df_marks.append(new_row, ignore_index=True)

print('\n\nNew row added to DataFrame\n--------------------------')
print(df_marks)


# persist to SQL lite 
conn = sqlite3.connect('test.db') # If the database does not exist, then it will be created and finally a database object will be returned.
print ("Opened database successfully")

#create table if not exists TableName (col1 typ1, ..., colN typN)

conn.execute('''CREATE TABLE IF NOT EXISTS HEAT
         (
         temperature_c           REAL    NOT NULL,
         temperature_f            REAL     NOT NULL);''')
print ("Table created successfully")

conn.execute("INSERT INTO HEAT (temperature_c,temperature_f) \
       VALUES (1.1, 100.1)");
print ("Test data inserted successfully")


conn.execute("INSERT INTO HEAT (temperature_c,temperature_f) VALUES (?, ?)",
          (temperature_c, temperature_f))
print ("Python data inserted successfully")

cursor = conn.execute("SELECT rowid, temperature_c, temperature_f FROM HEAT")
for row in cursor:
   print ("rowid = ", row[0])
   print ("temperature_c = ", row[1])
   print ("temperature_f = ", row[2])
print ("Data read successfully")

conn.close()
