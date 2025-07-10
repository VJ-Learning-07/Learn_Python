import random
L=[('''  
     _______
 ---'   ____)
       (_____)
 ROCK  (_____)
       (____)
 ---.__(___)
'''),

('''
      _______
 ---'    ____)____
            ______)
  PAPER    _______)
          _______)
 ---.__________)
'''),

(''' 
    _______
 ---'   ____)____
           ______)
 SCISSORS_________)
       (____)
 ---.__(___)
''')
]
choice=int(input("What do you Choose ? Type 0 for Rock , 1 for Paper and 2 for Scissors \n "))
print("Your choice ")
print(L[choice])
print("Computers choice  :")
CC=random.randint(0,2)
print(L[CC])
if choice==CC:
    print("IT's a Draw")
elif choice==0 and CC==1:
    print("You Loose")
    
elif choice==1 and CC==2:
    print(" You Loose")
elif choice==2 and CC==0:
    print("You Loose")
    
else:
    print("YAY \n You Win")        