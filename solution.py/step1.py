import random
import hangman_words
hangman_stages = hangman_stages_inverted = hangman_stages = [
    # Step 1 - Full Hangman (Game Over)
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    # Step 2 - Missing one leg
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    # Step 3 - Missing both legs
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    # Step 4 - Only one arm
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    # Step 5 - No arms
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    # Step 6 - Only head
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    # Step 7 - Empty Gallows (Start of Game)
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]

life=7
c = random.choice(hangman_words.words)
print("fron this you are to guess ::")
s=''
list=[]
for _ in range(len(c)):
    s+="_ "
    list.append("_")
print(s)   
gm=1
while gm:
    if life-1==0:
        print("game over \n You Lost , The man is dead ")
        print(c)
        break
    i = input("Enter a letter to match: ")
    answer=""
    for j in range(len(c)):
        if i.lower() == c[j]:
            list[j]=i
        
    if i.lower() not in list:
        life-=1           
    print(hangman_stages[life-1]) 
    print(f"lifes left={life-1}")   
    x=" ".join(list)
    print(x)
    if "_" not in x:
        print("game over")
        gm=0  
              
