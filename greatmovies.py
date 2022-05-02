from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all(name="h3", class_="title")

with open("movielist.txt", mode="w") as file:
    for movie in articles[::-1]:
        file.write(f"{movie.getText()}\n")
