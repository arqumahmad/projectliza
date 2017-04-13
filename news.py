#https://newsapi.org/v1/articles?source=techcrunch&apiKey=773c852ac3b94e46869da137d176a37d
#https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey=773c852ac3b94e46869da137d176a37d
import urllib2
import json

response = urllib2.urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey=773c852ac3b94e46869da137d176a37d')
data = json.load(response)
for x in range(0,4):
    print data["articles"][x]["title"]
