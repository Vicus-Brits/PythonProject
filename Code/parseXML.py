import xml.etree.ElementTree as ET
import pandas as pd

myXML = 'C:/Users/cc099293/Documents/GitHub/PythonProject/Data/Weather1.xml'

tree = ET.parse(myXML)

print(tree)

root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

latitude = root.find('latitude')
temperature_c = root.find('temperature_c')
temperature_f = root.find('temperature_f')
feels_like_temperature_c = root.find('feels_like_temperature_c')
feels_like_temperature_f = root.find('feels_like_temperature_f')


print ("latitude", latitude.text) 
print ("temperature_c", temperature_c.text) 
print ("temperature_f", temperature_f.text) 
print ("feels_like_temperature_c", feels_like_temperature_c.text) 
print ("feels_like_temperature_f", feels_like_temperature_f.text) 

