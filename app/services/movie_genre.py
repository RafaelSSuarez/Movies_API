from collections import Counter, defaultdict

from app.core.utils import read_csv_file

def movie_genre_each_year(gross_income:str):
    """
    Returns a dict with the movie genre that earned most ot least money each year
    :param gross: "highest" or "lowest" income
    """
    movies = read_csv_file()
    if gross_income == "highest":
        default_gross = 0
        comparison_operator = ">"
    else:
        default_gross = float("inf")
        comparison_operator = "<"
    default_final = defaultdict(lambda:{"Genre":"",
                                        "Gross":default_gross})
    default_counter = defaultdict(Counter)
    for row in movies:
        if (year:=row["title_year"]) and (row["gross"].isdigit()):
            final = default_final[year]
            gross_counter = default_counter[year]
            genres = row["genres"].split("|")
            for genre in genres:
                gross_counter[genre] += int(row["gross"])
                if eval(f"gross_counter[genre] {comparison_operator} final['Gross']"):
                    final["Gross"] = gross_counter[genre]
                    final["Genre"] = genre
    return default_final
