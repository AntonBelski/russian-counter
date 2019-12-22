import os
import xml.etree.ElementTree as ET


tree = ET.parse('Вайнер - Печать Света.fb2')
root = tree.getroot()
print(root)

for paragraph in root.findall('p'):
    print(paragraph)
