from package.imdbrating import ImdbRating

class Movie:
    def __init__(self, id:str) -> None :
        rating = ImdbRating.get_rating(id).content

        self.id = id
        self.title = rating['fullTitle']
        self.ratingRottenTomatoes = int(rating['rottenTomatoes'])
        self.ratingMetacritic = int(rating['metacritic'])
        self.year = rating['year']
