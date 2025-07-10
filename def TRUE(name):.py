def TRUE(name):
    string=TRUE
    count=0
    for i in range(len(name)):
        if string[i].lower()==name[i]:
            count+=1
    return count


def calculate_love_score(name1,name2):
   d1= TRUE(name1)
   d2= TRUE(name2)
   print(d1*10+d2)
calculate_love_score('rat','cree')    