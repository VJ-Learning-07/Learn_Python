import random

import art


def compare(user,computer):
    if user==computer:
        return "its a draw"
    elif computer==0:
        return "You lose , opponet has a black jack"
    elif user==0:
        return "Win with a black jack"
    elif user>21:
        return "you went Over , You lose"
    elif computer>21:
        return "Opponent went over , You win"
    elif user>computer:
        return "YOU WIN "
    else:
        return "You lose"

def calculate_score(card):
    """Take a list of cards and return the score calculated from the cards """
    if sum(card)==21 and len(card)==2:
        return 0
    if 11 in card and sum(card)>21:

        card.remove(11)
        card.append(1)
    return sum(card)
def deal_card( ):
    """Returns a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your Final Hand : {user_cards} , and final score is : {user_score}")
    print(f"computer's final hand is : {computer_cards}, and final score is : {computer_score}")
    print(compare(user_score, computer_score))


while input("DO you want to play a game of Blackjack , type 'y' or 'n'"):
    print("\n"*100)
    print(art.logo)
    play_game()








