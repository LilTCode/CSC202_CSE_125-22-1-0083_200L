#A tip calculator project

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people should split the bill? ")

percentage = int(percentage_tip) / 100
tip = float(bill) - (float(bill) * float(percentage))

splitting = tip / int(people)

print(f"Each person should pay: ${round(splitting, 2)}")

