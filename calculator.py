print("""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

(Regular Calculator)
""")
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
        
def mul(a,b) :
    return(a*b)
def div(a,b):
    return(a/b)
dict={"+":add,"-":sub,"*":mul,"/":div}
decision='n'
while 1:
    if decision=='exit':
        break
    elif decision=='n':
        a=float(input("whats the first number ? : "))
    else:
        a=n    
    for key in dict.keys():
            print(key)
    key=input("Pick an Operation   :")
    b=float(input("What's the next number? : ")) 
    n=dict[key](a,b)
        
    print(f"{a}{key}{b}={dict[key](a,b)}") 
    decision=input("Type 'y' to continue with previous number and type 'n' to continue with new numbers and 'exit' to quit")
       
                   