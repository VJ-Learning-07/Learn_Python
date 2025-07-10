import random 


al=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Al=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sp=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_', '=', '+', '[', ']', '{', '}', ':', ';',',', '.', '?']
i1=int(input("How many letters would u like in your password ? \n "))
i2=int(input("How many symbols would u like ? \n"))
i3=int(input("How many numbers woud u like ? \n "))
# s=i1+i2+i3
password=[]
for i in range (1,i1+i2+i3):
    if i<=i1:
        password.append(random.choice(al))
    elif i<=i2+i1:
        password.append(random.choice(sp))
    elif i<=i2+i1+i3:
        password.append(random.choice(n))
    
print("Your Password is :  ")

print(''.join(password))      