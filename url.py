import requests
import time
from bs4 import BeautifulSoup

url = "https://novel101.com/novels/6b877c89-9c4b-413b-83a7-4ade67919337/chapters/4r0"
for i in range(537):
    aaa = requests.get(url)
    soup = BeautifulSoup(aaa.text, "html.parser")

    next_chapter = soup.find("a",class_="next-chapter")
    next_url = "https://novel101.com"+next_chapter["href"]
    with open("url.txt","a") as f:
        f.write(f"{next_url} \n")
    url = next_url
    time.sleep(1)
# chapter_title = soup.find("div",class_="chapter-title")

# body = soup.find("div",class_="body")
# text = body.find_all("p")

# print(chapter_title.text)
# for i in text:
#     print(i.text)