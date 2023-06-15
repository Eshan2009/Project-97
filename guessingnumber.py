import random
print("number guessing game")
number=random.randint(1,19)
chances=0
print("guess the number : ")
while chances<10:
    guess=int(input("enter your guess"))
    if guess==number:
        print("Congradulations")
        break
    elif guess<number:
        print("Your guess was low", guess)
    else:
        print("Your guess was high", guess)

    chances+=1

if not chances<10:
    print("you lost", number)