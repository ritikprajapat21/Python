import re

# Checks year is leap year or not
def isLeapYear(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

# Validate the date
def validateDate(day, month, year):
    # Validate the month entered
    if not (1 <= month and month <= 12):
        return False
    else:
        # To calculate the total days in a month
        if (month == 2):
            end = (29 if isLeapYear(year) else 28)
        elif (month in [4, 6, 9, 11]):
            end = 30
        else:
            end = 31
    # Checking day is valid
    if (1 <= day and day <= end):
        return True
    return False

# To format date in dd-month-yyyy
def formatDate(day, month, year):
    monthDic = {'1': "January", '2': "February", '3': "March", '4': "April", '5': "May", '6': "June",
                '7': "July", '8': "August", '9': "September", '10': "October", '11': "November", '12': "December"}
    return f"{day}-{monthDic[str(month)]}-{year}"

# RegEx for date
datere = re.compile("(\d{1,2})([-/])(\d{1,2}|[A-Z][a-z]{3,4})([-/])(\d{4})")

print("Enter a date:")
date = input()

try:
    dateTuple = datere.search(date).groups()
    day, month, year = [int(dateTuple[0]), int(dateTuple[2]), int(dateTuple[4])]
except Exception as err:
    print(f"Enter correct date {err}")
else:
    if validateDate(day, month, year):
        print(formatDate(day, month, year))
    else:
        print("Enter correct date")