import requests
from package.responce import Response
from package.movie import Movie

class ImdbRequest:
    _base_url = "https://imdb-api.com/en/API/SearchMovie/"

    @classmethod
    def get_movies(cls, search:str, api_key:str = 'k_vg4yaklt') -> Movie:
        response = requests.get(cls._base_url + api_key + '/' + search)
        
        if response.status_code != 200:
            raise NameError('API Unavailable')

        imdbResponse = Response(status_code=response.status_code,
                          content=response.json())

        if imdbResponse.content['results'] == None:
            raise NameError(imdbResponse.content['errorMessage'])

        movies=[]
        for movie in imdbResponse.content['results']:
            if movie != None:
                movies.append(Movie(id=movie.get('id'), image=movie.get('image')))

        return movies