#!/usr/bin/python3
# A script to calculate the numbers of days lived for your present age

# Using a function to intialize the conditions for a leap year  
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

# Creating a funtion to list the leap years 
def find_leap(year_of_birth, age):
    leap_years= []
    for year in range(year_of_birth, year_of_birth + age):
        if leap_year(year):
            leap_years.append(year)
    return leap_years

# Creating a function to calculate the number of days lived 
def age_in_days(age):
    days_in_year= 365
    leap_years= find_leap(1, age)
    total_days= 0
    while age > 0:
        total_days += days_in_year
        if age in leap_years:
            total_days += 1
        age -= 1
    return  total_days

# Assigning variables for the passed parameters and declaring the function
if __name__ == "__main__":
    person_age = int()
    total_days= age_in_days(person_age)
    print(f"{total_days} days living on the earth!")         
