import requests
from bs4 import BeautifulSoup
import time

text = "邛籠石影 筆跡 https://novel101.com/novels/6b877c89-9c4b-413b-83a7-4ade67919337/chapters/2cjc"
text = text.split()
book = text[0]
chapter = text[1]
url = text[2]
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
content = soup.find("div",class_ = "body")
print(content.text)