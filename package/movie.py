class Movie:
    def __init__(self, id:str, title:str, rating=None) -> None :
        self.id = id
        self.title = title
        self.rating = rating