height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI_calculator = weight / (height ** 2)

if BMI_calculator < 18.5:
    print(f"Your BMI is {BMI_calculator}, you're underweight")
elif BMI_calculator < 25:
    print(f"Your BMI is {BMI_calculator}, you're normal weight")
elif BMI_calculator < 30:
    print(f"Your BMI is {BMI_calculator}, you're overweight")
elif BMI_calculator < 35:
    print(f"Your BMI is {BMI_calculator}, you're obese")
else:
    print(f"Your BMI is {BMI_calculator}, you're clinically obese")