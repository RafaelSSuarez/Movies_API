from csv import DictReader

from app.core.constants import DATA


def read_csv_file():
    """
    Read csv file with DictReader
    :return: csv DictReader
    """
    DATA.seek(0)
    movies = DictReader(DATA)
    return movies

def sort_csv_reader(
        reader:DictReader,
        column_name:str, 
        reverse:bool = False) -> list:
    """
    Sorts a CSV reader by a specific numeric column
    :param reader: csv DictReader
    :param column_name: The name of the column to sort with
    :param reverse: Boolean value, if True, the csv reader is sorted from highest to lowest
                    else, is sorted from lowest to highest
    :return: Sorted list of dictionaries
    """
    return sorted(
                filter(lambda x: x[column_name].isdigit(),reader), 
                key=lambda x: int(x[column_name]), 
                reverse=reverse
            )