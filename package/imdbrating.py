import requests
from package.response import Response


class ImdbRating:
    _base_url = "https://imdb-api.com/en/API/Ratings/k_vg4yaklt/"

    @classmethod
    def get_rating(cls, id):
        response = requests.get(cls._base_url+id)

        return Response(status_code=response.status_code, content=response.json())
