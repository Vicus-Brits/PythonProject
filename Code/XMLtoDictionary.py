#complete tutorial -- https://www.datacamp.com/community/tutorials/python-xml-elementtree

import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/cc099293/Documents/GitHub/PythonProject/Data/Movies.xml')
root = tree.getroot()

#for child in root:
   # print(child.tag, child.attrib)

   # print(ET.tostring(root, encoding='utf8').decode('utf8'))

#for movie in root.iter('movie'):
 #   print(movie.attrib)

for description in root.iter('description'):
    print(description.text)


