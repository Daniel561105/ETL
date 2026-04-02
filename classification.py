import requests
from bs4 import BeautifulSoup
import time

with open("name_url.txt","r",encoding="utf-8") as f:
    for text in f:
        text = text.split()
        book = text[0]
        chapter = text[1]
        url = text[2]
        if book == "邛籠石影":
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            content = soup.find("div",class_ = "body")
            with open(f"{book}.txt","a",encoding = "utf-8") as f:
                f.write(f"\n{chapter}\n")
                f.write(content.text)
                time.sleep(2)