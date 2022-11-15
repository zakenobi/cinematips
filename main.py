from package.imdbrequest import ImdbRequest


def main():
    movies = ImdbRequest.get_movies()

    print(movies.content['results'][0].get('id'))

main()
