from xml.dom import minidom

 #parse an xml file by name
file = minidom.parse('map.svg')

#use getElementsByTagName() to get tag
kommune_path_list = file.getElementsByTagName('path')




for kommune_path in kommune_path_list:


    current_val = kommune_path.attributes['style'].value
    new_current_val = current_val[:-4]
    new_current_val += "black; stroke-width:1px"

    kommune_path.attributes["style"].value = new_current_val

    new_current_val = ""

    



# with open('map.svg', 'w') as f:
#     f.write(file.toxml())