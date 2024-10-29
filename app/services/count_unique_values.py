import csv
import time

from app.core.constants import DATA


def count_unique_values(column: str):
    """
    Returns a dictionary with the respective count of unique values in a specific column
    :param column: The name of the specific column
    :return: Dictionary whose keys are uniques values of the column and the values are 
            the respective count
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