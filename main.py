import math
import random
import time

symbols = {
    "melon": "🍉",
    "cherry": "🍒",
    "bell": "🔔",
    "seven": "7️⃣"
}
list1 = ["melon", "cherry", "bell", "seven"]
balance = 100


def spin(bet):
    global balance
    line1 = random.choice(list1)
    line2 = random.choice(list1)
    line3 = random.choice(list1)
    time.sleep(1)
    print(
        f"Spinning... \n| {symbols[line1]} | {symbols[line2]} | {symbols[line3]} |")
    time.sleep(1)
    if line1 == line2 == line3:
        if line1 == "melon":
            win = bet * 2
            print(f"Congrats! 3 melons! +{win}$")
        elif line1 == "cherry":
            win = bet * 3
            print(f"Congrats! 3 cherries! +{win}$")
        elif line1 == "bell":
            win = bet * 5
            print(f"Congrats! 3 bells! +{win}$")
        elif line1 == "seven":
            win = bet * 10
            print(f"JACKPOT!!! 3 sevens! +{win}$")
        balance += win
    elif line1 == line2 or line2 == line3 or line3 == line1:
        win = bet // 2
        print(f"Nice! You got 2 matching symbols. +{win}$")
        balance += win
    else:
        print("Try again! ")


print("Hello! Do you want to play? ")
while True:
    if balance == 0 or balance < 0:
        print("Sorry, but you have no money! ")
        break
    print(f"Your balance is {balance}$")
    bet_input = input("Enter your bet (or 'exit' to quit): ")
    if bet_input.lower() == "exit":
        break
    try:
        bet = int(bet_input)
        if bet <= 0:
            print("Bet must be positive!")
            continue
        if bet > balance:
            print("You don't have enough money for that bet.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue
    balance -= bet
    print(f"Lets go! Your balance is {balance}$")
    spin(bet)
