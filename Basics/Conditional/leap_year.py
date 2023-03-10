year = int(input("please enter a year to check: "))

if year%4 ==0 :
    if year%100 ==0 and year%400 ==0:
        print(f"{year} is a leap year")
    elif year%100 !=0 and year%400 !=0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")


# another solution
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")

