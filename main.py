from bs4 import BeautifulSoup
import requests
import lxml

WEBSITE = "https://www.billboard.com/charts/hot-100/"

date_input = input("What year would you like to travel? Type the date in this format YYYY-MM-DD: ") +"/"

response = requests.get(WEBSITE + date_input)
web_page = response.text
soup = BeautifulSoup(web_page, "lxml")

title_tags = soup.select("li ul li h3")
title_text = [title_tag.getText().strip() for title_tag in title_tags]

print(title_text)