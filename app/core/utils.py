from collections import defaultdict
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

def extract_actors_info(
        row:dict,
        actor_number:int, 
        default_dict:defaultdict) -> None:
    """
    Save information about actors of a movie in a default dictionary
    :param row: Dictionary with information about a movie 
    :param actor_number: The number assigned to the actor in the dictionary
    :param default_dict: Dictionary where actors information is going to be saved
    """
    actor_name = row[f'actor_{actor_number}_name'].strip()
    if actor_name:
        actor_info = default_dict[actor_name] #actor_info is the deafult dict for the actor
        actor_info['number of movies'] += 1
        if not actor_info['facebook likes']: actor_info['facebook likes'] = row[f'actor_{actor_number}_facebook_likes']
        imdb_score = float(row['imdb_score'])
        if actor_info['best movie imdb score'] < imdb_score:
            actor_info['best movie imdb score'] = imdb_score
            actor_info['best movie'] = row['movie_title']
    if actor_number != 3:
        extract_actors_info(
            row=row,
            actor_number=actor_number+1,
            default_dict=default_dict)
    return
