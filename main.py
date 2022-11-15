from package.imdbrequest import ImdbRequest
from package.movie import Movie


def main():
    movies = ImdbRequest.get_movies(search="Inception 2010")

    print(movies.content)
    print(movies.content['results'][0])

    movie = Movie(
        id=movies.content['results'][0].get('id'),
        title=movies.content['results'][0].get('title')
    )

    

main()
