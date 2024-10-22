import csv

from app.core.settings import settings


def count_director_films():
    result = {}
    with open(settings.CSV_FILE_PATH, 'r') as m:
        movies = csv.DictReader(m)
        directors = [row['director_name'] for row in movies]
    uniques_directors = set(directors)
    for director in uniques_directors:
        result.update({director:directors.count(director)})
    return result