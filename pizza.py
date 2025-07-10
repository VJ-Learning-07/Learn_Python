print("welcome to the pizza galary ")
size=(input("what is the size of the pizza , M<S<L?"))
pepperoni=(input("DO ypu want pepperoni on your pizza ore onot Y or N"))
extra_cheeze=input("Do you want extra cheeze or not Y or N ")
bill=0
if size.upper()=='S':
    bill+=15
    if pepperoni.upper()=='Y':
        bill+=2
    if extra_cheeze.upper()=='Y':
        bill+=1
if size.upper()=='M':
    bill+=20
    if pepperoni.upper()=='Y':
        bill+=3
    if extra_cheeze.upper()=='Y':
        bill+=1
if size.upper()=='L':
    bill+=25
    if pepperoni.upper()=='Y':
        bill+=3
    if extra_cheeze.upper()=='Y':
        bill+=1        
print(f"total price of youtr pizza is : {bill}")        