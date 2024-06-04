print("Welcome to Treasure Island. \n Your mission is to find the treasure \n!lower cases for all inputs. Take note!\n")

way = input("Do you want to go left or right? \n")

if way == "right":
    print("You fell into a hole! Game over :) \n Sorry lad.")   
elif way == "left":
    next = input("You've made it to the next step! Do you want to swim or wait? \n")
    if next == "swim":
        print("You were attacked by a trout! Game over :) \n Sorry lad.")
    
    elif next == "wait":
        nextstep = input("You're very good. You've made it. Which door are you passing through? Red, Blue, or Yellow? ")
        if nextstep == "blue":
            print("You were eaten by beasts! Game over :) \n Sorry lad.")
        elif nextstep == "red":
            print("You were burned down by a fire! Game over :) \n Sorry lad.")
        elif nextstep == "yellow":
            print("Congrats! You won. Congrats on finding the treasure! :)")
        else:
            print("You lost because you didn't choose right!")
    else:
        print("You lost because you didn't choose right!")
else:
    print("You lost because you didn't choose right!")


