from unittest.mock import PropertyMock
from faker import Faker
import random

fake = Faker ()
genre_list = ["action", "adventure", "comedy", "drama", "fantasy", "horror", "musicals", "mystery", "romance", "science fiction", "sports", "thriller", "Western"]

class Movie ():
    def __init__(self, title, release, genre):
        self._title = title
        self.release = release
        self.genre = genre
        self._play_counter = 0

    def __str__(self):
        return f'{self._title} {self.release} {self.genre} {self._play_counter}'

    @property
    def title(self):
        return self._title

    @property
    def play_counter(self):
        return self._play_counter

    @play_counter.setter
    def play_counter (self, number):
        self._play_counter = number
    
    def play(self):
        self._play_counter += 1
        print(f'Obejrzałeś {self._title} ({self.release})')
        print(self._play_counter)

class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode


    def __str__(self):
        return f'{self._title} {self.release} {self.genre} {self.season}{self.episode} {self._play_counter}'

    def play(self):
        self._play_counter += 1
        print(f'Obejrzałeś {self._title} {self.season}{self.episode}')
        print(self._play_counter)


class Library ():
    def __init__(self):
        self.lista = []
    
    def add(self, object):
        if not (type(object) == Movie or type(object) == Series): 
            raise ValueError("neither a Movie nor Series")
        self.lista.append(object)
    
    def get_movies(self):
        return sorted([i for i in self.lista if type(i) == Movie], key = lambda pomidorowa: pomidorowa.title)

    def get_series(self):
        return sorted([i for i in self.lista if type(i) == Series], key = lambda pomidorowa: pomidorowa.title)

    def print_movies(self):
        for movie in self.lista:
            print (movie)

    def search(self, title):
        for item in self.lista:
            if item.title == title:
                return item
        raise Exception("Nie znaleziono")

    def generate_views(self):
        chosen_item = random.choice(self.lista)
        new_count = chosen_item.play_counter + random.randint(1, 100)
        chosen_item.play_counter=new_count
        return chosen_item.title, chosen_item.play_counter

    def generate_views_10x(self):
        for i in range (10):
            self.generate_views()


    def top_titles (self, number):
        top = sorted(self.lista, key = lambda ogorkowa: ogorkowa.play_counter, reverse=True)  
        return top[0:number]
    


def create_entertainment(what,x):
    entertainment = []
    for i in range(x):
        if what == "movie":
            entertainment.append(Movie(title = fake.sentence(nb_words=2), release = random.randint(1950, 2022), genre = random.choice(genre_list)))
        elif what == "series":
            num_of_s = random.randint(1, 10)
            num_of_e = random.randint(3, 20)
            entertainment.append(Series(title = fake.color_name(), release = random.randint(1950, 2022),genre = random.choice(genre_list),season = f'S{num_of_s:02}', episode = f'E{num_of_e:02}'))
    return entertainment




def main():
    print("biblioteka filmow")
    Hani = Library()
    x=10
    entMovie = create_entertainment("movie", x)
    entSeries = create_entertainment("series", x)
    for i in range(x):
        Hani.add(entMovie[i])
    for i in range(x):
        Hani.add(entSeries[i])
    
    Hani.generate_views_10x()
    print(Hani.top_titles(3))

main()    



