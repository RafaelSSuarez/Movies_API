import csv
import time

from app.core.settings import settings
from app.core.utils import sort_csv_reader


def sort_by_column(
        column_name:str,
        limit:int, 
        highest_first:bool = False):
    start = time.time()
    result = []
    with open(settings.CSV_FILE_PATH, 'r') as m:
        movies = csv.DictReader(m)
        movies=sort_csv_reader(movies,column_name, highest_first)       
    for row in movies:
        try:
            int_value = int(row[column_name])
        except ValueError:
            pass
        else:
            result.append({'movie_title':row['movie_title'],
                           f'{column_name}':int_value})
            if len(result) == limit:
                end = time.time()
                print(f'{end-start} seconds')
                return result