'''
In this Bite we are going to parse a movie dataset (csv) to identify the directors with the highest rated movies.

1. Write get_movies_by_director: use csv.DictReader to convert movie_metadata.csv into a (default)dict of Movie
namedtuple lists. Only extract director_name, movie_title, title_year and imdb_score. Filter out any missing or wrong
data: title_year needs to be int, imdb_score needs to be float. Discard any movies older than 1960.

Here is an extract:

....
{ 'Woody Allen': [
Movie(title='Midnight in Paris', year=2011, score=7.7),
Movie(title='The Curse of the Jade Scorpion', year=2001, score=6.8),
Movie(title='To Rome with Love', year=2012, score=6.3), ....
], ...
}

2. Write the calc_mean_score helper that takes a list of Movie namedtuples and calculates the mean (imdb) score, return
the score rounded to 1 decimal place.

3. Complete get_average_scores which takes the directors data structure returned by get_movies_by_director (1.) and
returns a list of tuples (director, average_score) ordered by highest score in descending order. Only take directors
into account with >= MIN_MOVIES
'''

import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = defaultdict(list)
    with open(MOVIE_DATA) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            if year and year < MIN_YEAR:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    ratings = [m.score for m in movies]
    mean = sum(ratings) / max(1, len(ratings))
    return round(mean, 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    ret = {director: calc_mean_score(movies)
           for director, movies in directors.items()
           if len(movies) >= MIN_MOVIES}
    return sorted(ret.items(), key=lambda x: x[1], reverse=True)

print(get_movies_by_director())


'''
director_movies = get_movies_by_director()


def test_get_movies_by_director():
    assert 'Sergio Leone' in director_movies
    assert len(director_movies['Sergio Leone']) == 4
    assert len(director_movies['Peter Jackson']) == 12


def test_director_movies_data_structure():
    assert type(director_movies) in (dict, defaultdict)
    assert type(director_movies['Peter Jackson']) == list
    assert type(director_movies['Peter Jackson'][0]) == Movie


def test_calc_mean_score():
    movies_sergio = director_movies['Sergio Leone']
    movies_nolan = director_movies['Christopher Nolan']
    assert calc_mean_score(movies_sergio) == 8.5
    assert calc_mean_score(movies_nolan) == 8.4


def test_get_average_scores():
    avg_scores = get_average_scores(director_movies)[:10]
    expected = [('Sergio Leone', 8.5),
                ('Christopher Nolan', 8.4),
                ('Quentin Tarantino', 8.2),
                ('Hayao Miyazaki', 8.2),
                ('Frank Darabont', 8.0),
                ('Stanley Kubrick', 8.0),
                ('James Cameron', 7.9),
                ('Joss Whedon', 7.9),
                ('Alejandro G. Iñárritu', 7.8),
                ('Alfonso Cuarón', 7.8)]
    assert avg_scores == expected
'''