MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

def get_deposit():
    while True:
        amount = input('How much would you like to deposit?\n$')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('The initial deposit must be greater than $0.')
        else:
            print('The deposit must be a number (non-decimal)')
    return amount

def get_bet_lines():
    while True:
        lines = input(f'How many lines would you like to bet on? (1-{MAX_LINES})\n')
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print(f'The amount of lines must be between 1 and {MAX_LINES}')
        else:
            print(f'Please enter a number between 1 and {MAX_LINES}')
    return lines 

def get_bet_per_line():
    while True:
        bet = input(f'How much would you like to bet on each line?\n$')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'The bet must be between ${MIN_BET} and ${MAX_BET}.')
        else:
            print('The bet must be a number (non-decimal)')
    return bet  

def calculate_total_bet(bet, lines):
    return bet * lines
       

def main():
    balance = get_deposit()
    bet_lines = get_bet_lines()
    while True:
        bet_per_line = get_bet_per_line()
        total_bet = calculate_total_bet(bet_per_line, bet_lines)
        if total_bet < balance:
            print(f'Bet: ${bet_per_line}.\nNumber of lines: {bet_lines}.\n Total bet: {total_bet}')
            break
        else:
            print(f"You don't have enough money to bet ${total_bet}. Your current balamce is ${balance}.")

main()