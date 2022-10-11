from unittest.mock import PropertyMock
from faker import Faker
import random
import datetime
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
        self._season = season
        self._episode = episode

    def __str__(self):
        return f'{self._title} {self.release} {self.genre} {self.season}{self.episode} {self._play_counter}'

    @property
    def season(self):
        return self._season

    @property
    def episode(self):
        return self._episode

    def play(self):
        self._play_counter += 1
        print(f'Obejrzałeś {self._title} {self.season}{self.episode}')
        print(self._play_counter)


class Library ():
    def __init__(self):
        self._lista = []
    
    @property
    def lista(self):
        return self._lista

    def add(self, object):
        if not (type(object) == Movie or type(object) == Series): 
            raise ValueError("neither a Movie nor Series")
        self._lista.append(object)
    
    def get_Movie(self):
        return sorted([i for i in self._lista if type(i) == Movie], key = lambda pomidorowa: pomidorowa.title)

    def get_series(self):
        return sorted([i for i in self._lista if type(i) == Series], key = lambda pomidorowa: pomidorowa.title)

    def print_Movie(self):
        for movie in self._lista:
            print (movie)

    def search(self, title):
        for item in self._lista:
            if item.title == title:
                print(f'Znaleziono {title}')
                return item
        
        raise Exception("Nie znaleziono")

    def generate_views(self):
        chosen_item = random.choice(self._lista)
        new_count = chosen_item.play_counter + random.randint(1, 100)
        chosen_item.play_counter=new_count
        return chosen_item.title, chosen_item.play_counter

    def generate_views_10x(self):
        for i in range (10):
            self.generate_views()

    def printuj(self):
        for i in self._lista:
            print (i)

    def top_titles (self, content_type, number):
        x = datetime.datetime.now().strftime("%d.%m.%Y")
        top = sorted(self._lista, key = lambda ogorkowa: ogorkowa.play_counter, reverse=True)
        the_best = top[0:number]
        print(f"Najpopularniejsze filmy i seriale dnia {x}:")
        for film in the_best:
            print (film.title)
        if content_type == "movie":
            top_m = []
            for movie in top:
                if type(movie) == Movie:
                    top_m.append(movie)
            the_best_m = top_m[0:number]
            print(f"Najpopularniejsze filmy dnia {x}:")
            for i in the_best_m:
                print(i.title)
        elif content_type == "series":
            top_s = []
            for series in top:
                if type(series) == Series:
                    top_s.append(series)
            the_best_s = top_s[0:number]
            print(f"Najpopularniejsze seriale dnia {x}:")
            for i in the_best_s:
                print(i.title)            

        else:
            raise ValueError("neither a movie nor series")
        
    

if __name__ == "__main__":
    pass

#filmy wykreowane z fakera:
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
    return entertainment
#filmy rzeczywiste na potrzeby funkcji "search"
prawdziwe = [
Movie(title = 'Tie Me Up! Tie Me Down!', release = 1990, genre = 'Comedy'),
Movie(title = 'High Heels', release = 1991, genre = 'Comedy'),
Movie(title = 'Dead Zone  The', release = 1983, genre = 'Horror'),
Movie(title = 'Cuba', release = 1979, genre = 'Action'),
Movie(title = 'Days of Heaven', release = 1978, genre = 'Drama' ),
Movie(title = 'Octopussy', release = 1983, genre = 'Action' ),
Movie(title = 'Target Eagle', release = 1984, genre = 'Action' ),
Movie(title = 'American Angels: Baptism of Blood  The', release = 1989, genre = 'Drama' ),
Movie(title = 'Subway', release = 1985, genre = 'Drama' ),
Movie(title = 'Camille Claudel', release = 1990, genre = 'Drama' ),
Movie(title = 'Fanny and Alexander', release = 1982, genre = 'Drama' ),
Movie(title = 'Tragedy of a Ridiculous Man', release = 1982, genre = 'Drama' ),
Movie(title = 'A Man & a Woman', release = 1966, genre = 'Drama' ),
Movie(title = 'A Man & a Woman: Twenty releases Later', release = 1986, genre = 'Drama' ),
Movie(title = 'Blackmail', release = 1929, genre = 'Mystery' ),
Movie(title = 'Donovan s Reef', release = 1963, genre = 'Comedy' ),
Movie(title = 'Tucker: The Man & His Dream', release = 1988, genre = 'Drama' ),
Movie(title = 'Scrooged', release = 1988, genre = 'Comedy' ),
Movie(title = 'Running Man  The', release = 1987, genre = 'Science Fiction' ),
Movie(title = 'Raiders of the Lost Ark', release = 1981, genre = 'Action' ),
Movie(title = 'Predator 2', release = 1991, genre = 'Action' ),
Movie(title = 'Colors', release = 1988, genre = 'Drama' ),
Movie(title = 'Un Hombre y una Mujer', release = 1966, genre = 'Drama' ),
Movie(title = 'Official Story  The', release = 1985, genre = 'Drama' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S01', episode = 'E02' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S01', episode = 'E03' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S02', episode = 'E01' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S02', episode = 'E02' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S02', episode = 'E03' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S03', episode = 'E01' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S03', episode = 'E02' ),
Series(title = 'Gra o Tron', release = 2012, genre = 'Fantasy',season = 'S03', episode = 'E03' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S01', episode = 'E01' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S01', episode = 'E02' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S01', episode = 'E03' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S02', episode = 'E01' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S02', episode = 'E02' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S02', episode = 'E03' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S03', episode = 'E01' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S03', episode = 'E02' ),
Series(title = 'Rodzina Soprano', release = 2000, genre = 'Drama',season = 'S03', episode = 'E03' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S01', episode = 'E01' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S01', episode = 'E02' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S01', episode = 'E03' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S02', episode = 'E01' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S02', episode = 'E02' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S02', episode = 'E03' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S03', episode = 'E01' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S03', episode = 'E02' ),
Series(title = 'The Office', release = 2010, genre = 'Comedy',season = 'S03', episode = 'E03' ),
]

def main():
        
    Hani = Library()
                    #filmy wykreowane z fakera:
    x=5
    entMovie = create_entertainment("movie", x)
    entSeries = create_entertainment("series", x)
    for i in entMovie:
        Hani.add(i)
    for i in entSeries:
        Hani.add(i)
                    #filmy rzeczywiste na potrzeby funkcji "search"
    for i in prawdziwe:
        Hani.add(i)
    
    Hani.generate_views_10x()
    
    print("Biblioteka filmow")
    Hani.top_titles("series",3)
    Hani.search("The Office")

main()    



