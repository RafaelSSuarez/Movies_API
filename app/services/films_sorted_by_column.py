import csv

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
    DATA.seek(0)
    movies = csv.DictReader(DATA)
    movies=sort_csv_reader(movies,column_name, highest_first)       
    return [{'movie title':row['movie_title'],f'{column_name}':int(row[column_name])} for row in movies[:limit]]