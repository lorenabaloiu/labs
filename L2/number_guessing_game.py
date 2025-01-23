import random
x = (random.randint(1, 20))
y = int(input("Try to guess the number: "))
ok = 0
for i in range(5,0,-1):
    print(f"You have {i} guesses left!")
    if y < x:
        print("The number is too low!")
        y = int(input("Try to guess the number: "))
    else:
        if y > x:
            print("The number is too high!")
            y = int(input("Try to guess the number: "))
        else:
            print("You guessed the number!")
            ok = 1
            break
if ok == 0:
    print(f"You used all your guesses and didnt guessed the number! :(\nThe number was: {x}")