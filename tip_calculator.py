print("Werlcome to the tip calculator!")
total=int(input("what was the total bill ?"))
tip=int(input("How much percent tip would u like to give 10 ,12 or 15 ? "))
t=total - (total *(tip/100))
split=int(input("How many people to split the bill ?"))
t=t/split
print(f"Each person should pay {round(t,2)}")