#Program for a Pizza Order
#S = 15, m = 20, L = 25, ps = 2, pml = 3, c = 1
print("Welcome to Testimony's Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small_size = 15
medium_size = 20
large_size = 25
pepperoni_small = 2
pepperoni_ml = 3
cheese = 1


if size == "S":
    bill = small_size
    if add_pepperoni == "Y":
        bill = small_size + pepperoni_small
        if extra_cheese == "Y":
            bill = small_size + pepperoni_small + cheese
            print(f"Your bill is ${bill}")
        elif extra_cheese == "N": 
            print(f"Your bill is ${bill}")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = small_size + cheese
            print(f"Your bill is ${bill}")
        elif extra_cheese == "N": 
            print(f"Your bill is ${bill}")      
elif size == "M":
    bill = medium_size
    if add_pepperoni == "Y":
        bill = medium_size + pepperoni_ml
        if extra_cheese == "Y":
            bill = medium_size + pepperoni_ml + cheese
            print(f"Your bill is ${bill}") 
        elif extra_cheese == "N": 
            print(f"Your bill is ${bill}")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = medium_size + cheese
            print(f"Your bill is ${bill}")
        elif extra_cheese == "N": 
            print(f"Your bill is ${bill}")         
elif size == "L":
    bill = large_size
    if add_pepperoni == "Y":
        bill = large_size + pepperoni_ml
        if extra_cheese == "Y":
            bill = large_size + pepperoni_ml + cheese
            print(f"Your bill is ${bill}") 
        elif extra_cheese == "N": 
            print(f"Your bill is ${bill}")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = large_size + cheese
            print(f"Your bill is ${bill}")
        elif extra_cheese == "N": 
            print(f"Your bill is ${bill}")    
            

