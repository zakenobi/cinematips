import requests
from package.responce import Response
from package.movie import Movie

class ImdbRequest:
    _base_url = "https://imdb-api.com/en/API/SearchMovie/k_vg4yaklt/"

    @classmethod
    def get_movies(cls, search) -> Movie:
        response = requests.get(cls._base_url+search)

        movies = Response(status_code=response.status_code,
                          content=response.json())

        return Movie(id=movies.content['results'][0].get('id'))