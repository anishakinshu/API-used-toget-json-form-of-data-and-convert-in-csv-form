import requests
from bs4 import BeautifulSoup
import urllib2
import pprint
import json
import csv

import sys
#sys.setdefaultencoding("utf-8")

#sys.stdout=open("test.txt", "w")
'''url = ('https://newsapi.org/v2/top-headlines?'
        'sources=bbc-news&'
        'apiKey=b77f71821c1145148cb7880b60bd4ec3') '''      


url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=b77f71821c1145148cb7880b60bd4ec3')


def to_string(s):
    try:
        return str(s)
    except:
        #Change the encoding type if needed
return s.encode('utf-8')

response=requests.get(url)

#with open('file.txt', 'w') as f:
json_data = json.loads(response.content)
#print(response.json())

#print(json_data1)
#sys.stdout.close()

#text = response.json().read()

#pprint(json.loads(text))

'''for i in range(len(json_data)):
    print(json_data[i]['description'])
'''
json_data1 = json_data['articles']
file1 = open('/tmp/file_data.csv', 'w')

csvwriter = csv.writer(file1)

count = 0

for i in json_data1:
    if count == 0:
       header = i.keys()
       csvwriter.writerow(header)
       count += 1
    
    csvwriter.writerow(to_utf8(i.values()))
file1.close()       



 

