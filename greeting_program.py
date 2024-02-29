import datetime


def get_part_of_day(hour):
    if 5 <= hour < 12:
        return 'morning'
    elif 12 <= hour < 17:
        return 'afternoon'
    elif 17 <= hour < 21:
        return 'evening'
    else:
        return 'night'

name = input("What is your name? ")

current_time = datetime.datetime.now(12:45)
part_of_day = get_part_of_day(current_time.hour)

# Greet the user

print (f"Good {part_of_day},{name}")
