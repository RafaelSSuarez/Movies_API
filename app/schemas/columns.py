from enum import Enum


class RequiredIntColumns(str, Enum):
    num_critic_for_reviews = "num_critic_for_reviews"
    duration = "duration"
    gross = "gross"
    budget = "budget"
    