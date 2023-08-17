import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_page = response.content

soup = BeautifulSoup(empire_page, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
titles_list = [title.getText() for title in all_movies]
movies = titles_list[::-1]

with open("movies.txt", mode="w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
