import random 


al=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Al=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sp=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_', '=', '+', '[', ']', '{', '}', ':', ';',',', '.', '?']
i1=int(input("How many lower case letters would u like in your password ? \n "))
i4=int(input("How many upper case lettrs would u like in your passowrd ? \n"))
i2=int(input("How many symbols would u like ? \n"))
i3=int(input("How many numbers woud u like ? \n "))
# s=i1+i2+i3
password=[]
for i in range (i1):
    
        password.append(random.choice(al))
for i in range(i2):
        password.append(random.choice(sp))
for i in range(i3)  :      
        password.append(random.choice(n))
for i in range (i4):
        password.append(random.choice(Al))    
         
ps=[]
for i in range(i1+i2+i3+i4):
    j=random.choice(password)
    ps.append(j)
    password.remove(j)           
    
print("Your Password is :  ")
# print(password)   
# random.shuffle(password)     
print(''.join(ps))      