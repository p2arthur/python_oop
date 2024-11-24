class Movie:

    def __init__(self, title, rating):
        self.title = title
        self.rsting = rating

    def get_title(self):
        return self.title

    def set_title(self):


my_movie = Movie('Titanic', 4.2)


print(my_movie.get_title())