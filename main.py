import random

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


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbol_count.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = [[] for _ in range(cols)]

    for _ in range(cols):
        current_symbols = all_symbols[:]
        for _ in range(rows):
            if not current_symbols:
                break
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            columns[_].append(value)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end=" ")
            else:
                print(column[row])


def spin_result(lines, columns):
    winnings = 0

    for line in range(lines):
        line_symbols = set(columns[line])
        unique_symbols = set(line_symbols)

        if len(unique_symbols) == 1:
            symbol = unique_symbols.pop()
            winnings += symbol_count[symbol] * lines

    return winnings


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings = spin_result(lines, slots)
    balance += winnings - total_bet

    print(f"Spin result: You won ${winnings}!")
    print(f"Your new balance is: ${balance}")


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
        else:
            print("Amount must be greater than 0.")
    else:
        print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
        else:
            print("Enter a valid number of lines.")
    else:
        print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
        else:
            print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
    else:
        print("Please enter a number.")

    return amount


if __name__ == "__main__":
    main()
