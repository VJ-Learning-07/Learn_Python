import art
from game_data import data
import random
def compare(ab):
    return f" {ab["name"]} , a {ab['description']} from {ab['country']}"

print(art.logo)
score=0
game_status=True
account_b=random.choice(data)
while game_status:
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    print(f"Compare A :{compare(account_a)}")
    print(art.vs)
    print(f"Agsinst B :{compare(account_b)}")

    guess=input("Who has more followers ? Type 'a' or 'b' :")
    print("\n"*20)
    print(art.logo)
    afc=account_a["follower_count"]
    bfc=account_b["follower_count"]

    #check answer
    if afc>bfc and guess.lower()=='a':
        score+=1
        print(f"You're right! Current score {score}")
    elif bfc>afc and guess.lower()=='b':
        score+=1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_status=False

