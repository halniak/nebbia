
# keep the code DRY - Don't Repeat Yourself
import math
import sys

import requests

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return Trzpue for leap year, false for non leap"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Zwraca liczbę dni w miesiącu danego roku"""
    if not 1 <= month <= 12:
        return "Wrong month"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2017, 2))

r = requests.get("http://nebbia.bio")
print(r.status_code)
