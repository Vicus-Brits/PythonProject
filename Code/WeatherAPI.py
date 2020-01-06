## https://developer.weatherunlocked.com/signup

import requests
from requests import Response

weather_type: str = 'current'
call_string = 'http://api.weatherunlocked.com/api/' + weather_type + '/51.50,-0.12?app_id=0ca7c5a3&app_key=10fb8b0062bbcaf0934cedeb7a3cd23c'
 
response: Response = requests.get(call_string, headers={'Accept': 'text/xml'})

response.
print(response.status_code)

print(response.content)