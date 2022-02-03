"""from bs4 import BeautifulSoup


with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.title.string)

#print(soup.prettify())

#print(soup.p)

all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

#for tag in all_anchor_tags:
    #print(tag.getText())
    #print(tag.get("href"))
heading = soup.find(name="h1", id="name")
print(heading)

class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)"""

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="a", class_="storylink")
print(article_tag)




















