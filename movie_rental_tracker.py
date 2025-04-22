class Movie:
    def __init__(self, title, genre, rented):
        self.title = title
        self.genre = genre
        self.rented = rented

    def check_out(self):
        self.rented = True

    def return_movie(self):
        self.rented = False
    
    def __str__(self):
        status = "Rented" if self.rented else "Available"
        return f"{self.title} {self.genre} - ({status})"
    
movie1 = Movie("Inception", "Sci-Fi", False)
movie2 = Movie("The Godfather", "Crime", False)
movie3 = Movie("The Dark Knight", "Action", False)

movie1.check_out()
movie2.return_movie()
movie3.check_out()
movie3.return_movie()

print(movie1)
print(movie2)
print(movie3)