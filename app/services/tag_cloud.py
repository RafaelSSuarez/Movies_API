from collections import Counter

from app.core.utils import read_csv_file

def tag_cloud():
    """
    Returns a dictionary where keys are plot keywords and values are the respective number of appearances.
    The dictionary is sorted by number of appearances.
    :return: Sorted dictionary
    """
    movies = read_csv_file()
    cnt = Counter()
    for row in movies:
        if row['plot_keywords']:
            words = row['plot_keywords'].strip().split('|')
            for word in words:
                cnt[word]+=1
    return sorted(cnt.items(), key=lambda x:x[1], reverse=True)