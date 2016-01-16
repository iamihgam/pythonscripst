"""
writing  a program using BeautifulSoup to parse a html file
, isolate the numbers and calculate its sum
"""
import urllib.request
from bs4 import BeautifulSoup

# opening the test file and parse it contents
html= urllib.request.urlopen('http://python-data.dr-chuck.net/comments_213180.html').read()
soup = BeautifulSoup(html,'lxml')

# retrieve the numbers from the file and store it as list and doing summation
tags = soup.find_all("span", attrs= {"class":"comments"}) # zeroing in on the particular section
num = [tag.text for tag in tags]# zeroing in on the number and extracting it as a list
x=sum(int(i) for i in num) # convert them into number and sum it up
print(x) # voila the result
