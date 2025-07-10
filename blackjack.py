import random
import art

def fh():
    print(f"Your final hand:{player} , current score {sum(player)}")
    print(f"computer's final hand : {computer} , final score: {sum(computer)}")
cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
exitcode='y'
while exitcode.lower()=='y':
    exitcode=input("DO you want to play a game of Blackjack? type 'y' or 'n' :")
    if(exitcode=='y'):
        print(art.logo)
        player=[]
        computer=[]
        player.append(random.choice(cards))
        player.append(random.choice(cards))
        print(f"Your cards : {player} , current score:{sum(player)} ")
        computer.append(random.choice(cards))
        computer.append(random.choice(cards))
        print(f"Computers first card is :{computer[0]}")
        choice='y'
        while(sum(player)<22) and (sum(computer)<22):
            choice=input("Type 'y' to get another card , type 'n' to pass:")
            if(choice=='y'):
                player.append(random.choice(cards))
                print(f"Your cards :{player}, current score: {sum(player)}")
                if(sum(player)<22):
                    print(f"Computers first card is :{computer[0]}")
            else:
                break
        if choice=='n':

            while(sum(computer)<=16 ):
                if (sum(computer)>=sum(player)):
                    break
                computer.append(random.choice(cards))

        if sum(player)>21:
                print(f"computer's cards : {computer}, total is : {sum(computer)}")
                print("You went over , YOu loose")
        elif sum(player)==sum(computer)    :
            fh()
            print("IT's a draw")
        elif sum(computer)>21 or sum(player)>=sum(computer):
            fh()
            print("You Win ")

        else:
            fh()
            print("You Lose")
