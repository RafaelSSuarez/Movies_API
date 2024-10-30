import time

from app.core.utils import read_csv_file


def count_unique_values(column: str):
    """
    Returns a dictionary with the respective count of unique values in a specific column
    :param column: The name of the specific column
    :return: Dictionary whose keys are uniques values of the column and the values are 
            the respective count
    """
    t1 = time.time()
    result = {}   
    movies = read_csv_file()
    for row in movies:
        if row[column] == '':
            continue
        if row[column] not in result:
            result.update({row[column]:0})
        result[row[column]] += 1
    t2 = time.time()
    print(f'{t2-t1} seconds')
    return result