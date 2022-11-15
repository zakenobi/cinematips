from package.imdbrequest import ImdbRequest

def main():
    movies = ImdbRequest.get_movies(search="Star Wars")

    movies.sort(key=lambda x: x.ratingRottenTomatoes, reverse=True)

    for movie in movies:
        print(f"{movie.ratingRottenTomatoes} : {movie.title}")

main()
