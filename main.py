import os
from art import logo


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


should_go = True
dic_bid = {}
bigger = 0
while should_go:
    print(logo)
    name = input("What is your name:  ")
    bid_amount = int(input("What is your bid? :$"))
    dic_bid[name] = bid_amount

    if bid_amount > bigger:
        bigger = bid_amount

    is_go = input("Is there any other bidder? 'Yes' or 'No'").lower()
    if is_go == "no":
        should_go = False
    for name in dic_bid:
        if dic_bid[name] == bigger:
            winner = name

    clear()

print(f"The winner is {winner} with a bid of ${bigger}")




