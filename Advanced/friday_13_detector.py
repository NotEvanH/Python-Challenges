import datetime

def detect_one(month, year):
    return datetime.datetime(year, month, 13).weekday() == 4

def detect_two(month, year):
    # Uses zeller's congruence algorithm so no idea how this function actually works just copied what wikipedia said

    if month < 3:
        month += 12
        year -= 1

    K = year % 100
    J = year // 100

    day_of_week = (13 + (13 * (month + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)) % 7

    return day_of_week == 5

print(f'Solution 1: {detect_one(10, 2023)}')
print(f'Solution 2: {detect_two(8, 2024)}')