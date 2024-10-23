import csv
import time

from app.core.settings import settings


import csv
import time

from app.core.constants import DATA


def count_unique_values(column: str):
    """
    Returns a dictionary with the respective number of Color and
      Black and white movies
    """
    t1 = time.time()
    DATA.seek(0)
    result = {}   
    movies = csv.DictReader(DATA)
    for row in movies:
        if row[column] not in result:
            result.update({row[column]:0})
        result[row[column]] += 1
    t2 = time.time()
    print(f'{t2-t1} seconds')
    return result