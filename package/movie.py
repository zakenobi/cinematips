from package.imdbrating import ImdbRating

class Movie:
    def __init__(self, id:str) -> None :
        rating = ImdbRating.get_rating(id).content

        self.id = id
        self.title = rating['fullTitle']
        self.ratingRottenTomatoes = rating['rottenTomatoes']
        self.year = rating['year']
        self.ratingMetacritic = rating['metacritic']