class Movie:
    def __init__(self, title, year, lang=''):
        self.title = title
        self.year = year
        self.lang = lang


favorite_movie = Movie("Click", "2005", 'english')


print(favorite_movie.title, favorite_movie.year, favorite_movie.lang)
