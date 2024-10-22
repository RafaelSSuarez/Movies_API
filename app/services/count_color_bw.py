import csv

from app.core.settings import settings


def count_color_bw():
    """
    Returns a dictionary with the respective number of Color and
      Black and white movies
    """
    color: int = 0
    bw: int = 0
    with open(settings.CSV_FILE_PATH, 'r') as m:
        movies = csv.DictReader(m)
        for row in movies:
            row_parsed = row['color'].lower().replace(' ','')
            if row_parsed  == 'color':
                color += 1
            elif row_parsed == 'blackandwhite':
                bw += 1
    return {
        'Color':color,
        'Black and White':bw
    }
