import art
from game_data import data
import random
def compare(ab):
    r1=random.choice(data)
    print(f"{ab} : {r1["name"]} , a {r1['description']} from {r1['country']}")
    return r1['follower_count']

score=0
while 1:
    print(art.logo)
    if score>0:
        print(f"You're right! Current score {score}")
    elif score==-1:
        print("Sorry , that's wrong . Final score : 0 ")
        break
    a=compare("Compare A")
    print(art.vs)
    b=compare("Against B")
    i=input("Who has more followers ? Type 'A' or 'B' :")
    if a==max(a,b) and i.lower()=='a':
        score+=1
    elif b==max(a,b) and i.lower()=='b':
        score+=1
    else:
        score=-1
    print("\n"*100)

