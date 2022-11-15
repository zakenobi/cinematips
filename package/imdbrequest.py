import requests
from package.responce import Response
from package.movie import Movie

class ImdbRequest:
    _base_url = "https://imdb-api.com/en/API/SearchMovie/k_vg4yaklt/"

    @classmethod
    def get_movies(cls, search) -> Movie:
        response = requests.get(cls._base_url+search)

        imdbResponse = Response(status_code=response.status_code,
                          content=response.json())

        movies=[]
        for movie in imdbResponse.content['results']:
            movies.append(Movie(id=movie.get('id')))

        return movies