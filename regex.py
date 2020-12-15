"""
regex.py

"""

import re

s = 'Alex:1994, Kate:1996'
patten = '(\w+):(\d+)'

l = re.findall(patten,s)
print(l)

regex = re.compile(patten)
l = regex.findall(s,0,12)
print(l)

l = re.split(r'[:,]',s)
print(l)

# s = re.sub(r':','-',s)
# s = re.sub(r':','-',s,1)
s = re.subn(r':','-',s)
print(s)