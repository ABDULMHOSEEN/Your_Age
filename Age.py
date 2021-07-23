# import datatime and math
import datetime
from math import *

# print the function of the program
print("Hello I am (Age).")
print("My function is to tell your age by taking some information")

# define a function call age
def age():
    # take the year month and day from the computer
    year_PC = datetime.datetime.now().year
    month_PC = datetime.datetime.now().month
    day_PC = datetime.datetime.now().day

    # Take the users input and find the different to git age
    user_year = int(input('inter the year that you was born in: '))
    if user_year > year_PC:     # check
        print("Error year value")
    else:
        user_year = year_PC - user_year

        user_month = int(input("inter the month: "))
        if user_month > 12:     # check
            print("Error month value")
        else:       # check
            user_month = month_PC - user_month

            user_day = int(input('inter the day: '))
            if user_day > 31:
                print("Error day value")
            else:       # check
                user_day = day_PC - user_day

                # Make sure that the year are correct and see the different between months
                if user_month < 0:
                    user_year -= 1
                    user_month += 12
                if user_day < 0:
                    user_month -= 1
                    user_day += 28
                # print the output
                print("Your age is {} years {} months and {} days by English calendar".format(user_year, user_month, user_day))

                # take the age with decimal point to find the different between the two calender
                age_with_decimal = user_year+(user_month/10)
                different_between_calender = ceil((11.2*age_with_decimal)/28) + user_month
                # if the different is bigger than 12 months add 1 to year
                if different_between_calender > 12:
                    user_year += 1
                    different_between_calender -= 12
                print("your age is {} years and {} months by Arabic calendar".format(user_year, different_between_calender))

age()


