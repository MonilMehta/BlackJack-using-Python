cards_list = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from random import randint
from blackjack_ascii import logo

print(logo)

def deal_card():
    return cards_list[randint(0, len(cards_list) - 1)]

def total_count(card_list):
    total = sum(card_list)
    if total > 21 and 11 in card_list:
        total -= 10  # Convert one 11 to 1 if total is over 21
    return total

print("Welcome to Blackjack")

user_cards = []
comp_cards = []

# Initial dealing
user_cards.append(deal_card())
user_cards.append(deal_card())
comp_cards.append(deal_card())
comp_cards.append(deal_card())

game_end = False

print("Dealers Hand : ")
print(comp_cards[0],end=" ")
print("_")

while not game_end:
    print("Your Hand is:", user_cards)
    user_count = total_count(user_cards)
    print(f"Your total is {user_count}")

    if user_count == 21:
        print("Blackjack! You win!")
        game_end = True
        break
    elif user_count > 21:
        print("Bust! You lost.")
        game_end = True
        break

    user_choice = int(input("Press 1 for Hit, 0 for Stand: "))
    if user_choice == 0:
        break

    user_cards.append(deal_card())

while total_count(comp_cards) <= 16:
    comp_cards.append(deal_card())

comp_count = total_count(comp_cards)

print("\n")
print(f"Your Hand is {user_cards}")
print(f"Your Count is {user_count}")
print(f"Dealer's Hand is {comp_cards}")
print(f"Dealer's Count is {comp_count}")

if comp_count > 21:
    print("Dealer busts! You win.")
elif user_count > comp_count:
    print("You Win!")
elif user_count == comp_count:
    print("It's a Tie!")
else:
    print("You Lose.")
