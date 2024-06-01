#A program to detect a leap year

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("It is leap")
        else:
            print("It is not leap")
    else:
        print("It is leap!")
else:
    print("It is not leap")