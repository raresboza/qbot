import requests
import json


class moviedb:
    def __init__(self, api_key: str):
        self.key = api_key

    def search_movies(self, search: str):
        url = "https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&query={}&page=1&include_adult=false".format(self.key, search)
        url.replace(" ", "%20")

        response = requests.get(url)

        return response.text

    def get_details(self, movie_id: int):
        url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, self.key)

        # print(url)
        response = requests.get(url)

        return response.text
