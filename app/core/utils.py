from csv import DictReader
from operator import itemgetter


def sort_csv_reader(
        reader:DictReader,
        column_name:str, 
        reverse:bool = False) -> list:
    return sorted(
                filter(lambda x: x[column_name].isdigit(),reader), 
                key=lambda x: int(x[column_name]), 
                reverse=reverse
            )