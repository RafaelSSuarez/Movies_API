from collections import defaultdict

from app.core.utils import read_csv_file, extract_actors_info

def ranking(limit:int):
    """
    Returns an actor ranking sorted by the number of movies appearances.
    :param limit: number of actors
    :return: list of actors with their corresponding number of movies, facebook likes and best movie
    """
    ranking_dict = defaultdict(lambda:{'number of movies':0,
                                   'facebook likes':None,
                                   'best movie':None,
                                   'best movie imdb score':0})
    movies = read_csv_file()
    for row in movies:
        extract_actors_info(row=row,
                            actor_number=1,
                            default_dict=ranking_dict)
    result = sorted(ranking_dict.items(),key=lambda x: x[1]['number of movies'],reverse=True)
    return result[:limit]