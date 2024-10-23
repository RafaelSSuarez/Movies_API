import csv
import time

from app.core.constants import DATA
from app.core.utils import sort_csv_reader


def sort_by_column(
        column_name:str,
        limit:int, 
        highest_first:bool = False):
    """
    Resturns a list of dictionaries sorted by a specific column
    :param column_name: The name of the column to sort with
    :param limit: Maximun list length
    :param highest_first: Boolean value, if True, the csv reader is sorted from highest to lowest
                        else, is sorted from lowest to highest
    :return: Sorted list of dictionaries
    """
    t1 = time.time()
    DATA.seek(0)
    result = []
    movies = csv.DictReader(DATA)
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
                t2 = time.time()
                print(f'{t2-t1} seconds')
                return result