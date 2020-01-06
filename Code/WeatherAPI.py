## https://developer.weatherunlocked.com/signup

import requests
type = 'current'
callstring = 'http://api.weatherunlocked.com/api/'+type+'/51.50,-0.12?app_id=0ca7c5a3&app_key=10fb8b0062bbcaf0934cedeb7a3cd23c'
 
response = requests.get(callstring, headers={"Accept":"text/xml"})


print(response.status_code)

print(response.content)