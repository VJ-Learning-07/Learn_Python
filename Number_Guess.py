import random
import art
number=random.randint(1,100)
def check(num,gues):
    if num==gues:
        print("You got it ")
    elif gues>num  :
        print("TOO HIgh . \n GUess again")
    else:
        print("TOO LOW . \n Guess again")

print(art.logo)
print("Welcome to the number guessing game!")
print("I'm Thinking of a number between 1 and 100")
difficulty=input("Choose a difficulty . Type 'easy' or 'hard'::")
if difficulty=='easy':
    chances=10
else :
    chances=5
guess=-1
while chances!=0 and guess!=number:
    print(f"You have {chances} attempts remaining to guess your number .")
    guess=int(input("Make a guess : "))
    check(number,guess)
    chances-=1

if chances==0:
    print("You ran out of chances ")

