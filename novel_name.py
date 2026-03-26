import requests
from bs4 import BeautifulSoup
import time

with open("url.txt","r") as f:
    for url in f:
        url = url.strip()
        print(f"{url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        chapter_title = soup.find("div",class_="chapter-title")
        print(chapter_title.text)
        write_in_text = chapter_title.text.replace("·"," ").strip()
        with open("url_name.txt","a") as k:
            k.write(f"{write_in_text} {url} \n")
        # time.sleep(0.5)

