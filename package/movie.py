from package.imdbrating import ImdbRating


class Movie:
    def __init__(self, id: str, image: str) -> None:
        rating = ImdbRating.get_rating(id).content

        self.id = id
        self.image = image
        self.title = rating['fullTitle']
        intRating: int = 0
        try:
            intRating = int(rating['rottenTomatoes'])
        except EnvironmentError:
            intRating = 0

        self.ratingRottenTomatoes = intRating
        self.ratingMetacritic = rating['metacritic']
        self.year = rating['year']
