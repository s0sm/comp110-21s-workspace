"""A vaccination calculator."""

__author__ = "730411526"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
days_to_go = 0
population = int(input("Population: "))
doses = int(input("Doses administered: "))
dose_per_day = int(input("Doses per day: "))
target_percent = int(input("Target percent vaccinated: "))

days_to_go = ((population*(target_percent/100)*2)-doses)/dose_per_day
today: datetime = datetime.today()
days_until_goal: timedelta = timedelta(int(days_to_go))
goal_day: datetime = today + days_until_goal

date_time = goal_day.strftime("%B %d, %Y")
print("We will reach " + str(target_percent) + "% vaccination in " + str(round(days_to_go)) + " days, which falls on", date_time)
