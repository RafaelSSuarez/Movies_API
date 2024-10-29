from app.services.count_unique_values import count_unique_values


def year_most_or_least_films(desired_value: str):
    """
    Returns the year with the greatest number of films or the year with the least number of films
    :param desired_value: most films or least films
    :return: The desired year
    """
    years_dict = count_unique_values('title_year')
    keys = list(years_dict.keys())
    values = list(years_dict.values())
    if desired_value == 'most films':
        return keys[values.index(max(values))]
    else:
        return keys[values.index(min(values))]

    