import csv
import time

from app.core.settings import settings


def count_color_bw():
    color: int = 0
    bw: int = 0
    start = time.time()
    with open(settings.CSV_FILE_PATH, 'r') as m:
        movies = csv.DictReader(m)
        for row in movies:
            row_parsed = row['color'].lower().replace(' ','')
            if row_parsed  == 'color':
                color += 1
            elif row_parsed == 'blackandwhite':
                bw += 1
    end = time.time()
    print(f'{end-start} seconds')
    return {
        'Color':color,
        'Black and White':bw
    }
