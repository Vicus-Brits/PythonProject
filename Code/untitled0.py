## https://developer.weatherunlocked.com/signup

import requests
from requests import Response
import xml.etree.ElementTree as ET


# Get API data
weather_type: str = 'current'
call_string = 'http://api.weatherunlocked.com/api/' + weather_type + '/51.50,-0.12?app_id=0ca7c5a3&app_key=10fb8b0062bbcaf0934cedeb7a3cd23c'
 
response: Response = requests.get(call_string, headers={'Accept': 'text/xml'})
print(response.status_code)
print(response.content)


tree = ET.parse(response.content)
root = tree.getroot()

# all items data
print('Expertise Data:')

for elem in root:
   for subelem in elem:
      print(subelem.text)