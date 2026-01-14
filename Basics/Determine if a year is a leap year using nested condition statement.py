'''
Note: A year is a leap year if "any one of " the following conditions are satisfied: 
The year is multiple of 400.
The year is a multiple of 4 and not a multiple of 100.
400 == 0
100 == 1
4 == 0
'''

year = int(input("enter the year"))
if year %400 ==0:
    if year % 100 ==0:
        if year % 4 ==0:
            print(year,"it is a leap year")
        else:
            print(year,"it is not a leap year")
    else:
        print(year,"it is a leap year")
else:
    print(year,"not a leap year")
