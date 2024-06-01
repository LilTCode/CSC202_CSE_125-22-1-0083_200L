print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride!")
    age = int(input("What is your age: "))
    if age < 12:
        print("You're paying $5.")
    elif age <= 18:
        print("You're paying $7")
    else:
        print("You're paying $12.")
else:
    print("You're not tall enough to ride!")

