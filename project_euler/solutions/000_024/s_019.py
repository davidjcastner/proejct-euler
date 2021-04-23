# Counting Sundays
# Problem 19

# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


from project_euler.lib.dates import Date, increment_day


def solve(limit: int = 2000) -> str:
    '''Problem 19 - Counting Sundays'''
    current = Date(1, 1, 1900, 0)
    sundays = 0
    while current.year <= limit:
        if current.year >= 1901 and current.dayofweek == 6 and current.day == 1:
            sundays += 1
        current = increment_day(current)
    return str(sundays)


if __name__ == '__main__':
    print(solve())
