import requests
from package.responce import Response

class ImdbRequest:
    _base_url = "https://imdb-api.com/en/API/SearchMovie/k_vg4yaklt/"

    @classmethod
    def get_movies(cls, search):
        response = requests.get(cls._base_url+search)

        return Response(status_code=response.status_code, content=response.json())