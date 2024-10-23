from enum import Enum


class RequiredUniqueValuesColumns(str,Enum):
    color = "color"
    director_name = "director_name"

class RequiredIntColumns(str, Enum):
    num_critic_for_reviews = "num_critic_for_reviews"
    duration = "duration"
    gross = "gross"
    budget = "budget"
    