from datetime import datetime


def add_years(original_date: datetime, year_to_be_added):
    resulting_date = original_date.replace(year=original_date.year + year_to_be_added)

    return resulting_date