from faker import Faker
fake = Faker ()
import random
genre_list = ["action", "adventure", "comedy", "drama", "fantasy", "horror", "musicals", "mystery", "romance", "science fiction", "sports", "thriller", "Western"]
class Movie ():
    def __init__(self, title, release, genre):
        self.title = title
        self.release = release
        self.genre = genre
        self.play_counter = 0
    def __str__(self):
        return f'{self.title} {self.release} {self.genre} {self.play_counter}'
    def play(self):
        self.play_counter += 1
        return self.play_counter


class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode
    def __str__(self):
        return f'{self.title} {self.release} {self.genre} {self.season}{self.episode} {self.play_counter}'

# class Library ():
#     def __init__(self):
#         self._lista =[]

    
#     def add(self, object):
#         if not (genre(object) == Movie or genre(object) == Series): 
#             raise ValueError("neither a Movie nor Series")
#         self._lista.append(object)
    
#     def print_Movie(self):
#         for movie in self._lista:
#             print (movie)

#     def ile_ma_lista (self):
#         x = print(len(self._lista))
#         return x

def create_entertainment(what,x):
    entertainment = []
    for i in range(x):
        if what == "movie":
            entertainment.append(Movie(title = fake.sentence(nb_words=2), release = random.randint(1950, 2022), genre = random.choice(genre_list)))
        elif what == "series":
            Title = fake.color_name()
            Release = random.randint(1950, 2022)
            Genre = random.choice(genre_list)
            num_of_s = random.randint(1, 10)
            num_of_e = random.randint(3, 20)
            for s in range(1,num_of_s+1):
                for e in range(1,num_of_e+1):
                    entertainment.append(Series(title = Title, release = Release, genre = Genre, season = f'S{s:02}', episode = f'E{e:02}'))
    # print(len(entertainment))
    return entertainment



# num_of_s = random.randint(1, 10)
# num_of_e = random.randint(3, 20)
# print(num_of_s)
# print(num_of_e)

# title = fake.color_name()
# release = random.randint(1950, 2022)
# genre = random.choice(genre_list)

# for s in range(1,num_of_s+1):
#     for e in range(1,num_of_e+1):
#         print(f'{title} S{s:02} E{e:02}')


entMovie = create_entertainment("movie", 5)
entSeries = create_entertainment("series", 5)





# m = Movie(title = "Plac Zbawiciela", release = 2006, genre = "dramat")
# s = Series(title = "Mentalist", release = 2008, genre = "crime", season = "S01", episode = "E01")
# mm = Movie(title = "Diuna", release = 2021, genre = "Sci-fi/Adventure")

