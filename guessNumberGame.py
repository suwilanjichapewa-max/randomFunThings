import random
num = random.randint(1,100)

print("welcome to the game. you have 3 tries to guess the number. it lies between 1 and 100")

guess = input("ener your 1st guess: ")
ques(num)
guess = input("ener your 2nd guess: ")
ques(num)
guess = input("ener your final guess: ")
print(f"you lose. the number was {num}")

def ques(num):
    if guess > num:
        print("Go lower!")
    elif guess < num:
        print("Go higer!")
    else: 
        print("you win")
        exit




