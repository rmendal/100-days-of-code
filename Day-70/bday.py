from calendar import day_name
from datetime import date

def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    day = day_name[date.weekday()]
    return day

if __name__ == '__main__':
    weekday_of_birth_date(date(1976, 4, 21))
