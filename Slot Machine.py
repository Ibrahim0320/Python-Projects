# A project that will basically allow players to bet on lines
# will comprise of base python in order to improve a pratical
# understanding of functions and such

# https://www.youtube.com/watch?v=th4OBktqK1I&ab_channel=TechWithTim 

import random as rd 


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}



def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines







def get_slotmachine_spin(rows, cols, symbols):
    all_symbols = []
    current_symbols = all_symbols[:]
    for symbol, symbol_count in symbols.items:
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns = [[], [], []]
    for col in range(cols):
        column = []
        for row in range(rows):
            value = rd.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns


def print_slotmachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="")
             




def deposit():  
    while True:
        amount = input("What would you like to deposit?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Chosen lines chosen be greater than 0.")
        else:
            print("Please enter a number of lines")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - {MAX_BET}$.")
        else:
            print("Please enter a number")

        return amount


def spin(balance):
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough balance to bet that amount. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting on ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")


    slots = get_slotmachine_spin(ROWS, COLS, symbol_count)
    print_slotmachine(slots)
    winnings, winning_lines  = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()
