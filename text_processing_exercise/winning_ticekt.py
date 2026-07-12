def valid_ticket(ticket: str) -> bool:
    if len(ticket) == 20:
        return True
    return False

def winning_ticket(ticket: str) -> bool:
    left_part = ticket[0:10]
    right_part = ticket[10:]
    for count in range(9, 5, -1):
        if ("@" * count) in left_part and ("@" * count) in right_part:
            return True, "@", count
        elif ("#" * count) in left_part and ("#" * count) in right_part:
            return True, "#", count
        elif ("$" * count) in left_part and ("$" * count) in right_part:
            return True, "$", count
        elif ("^" * count) in left_part and ("^" * count) in right_part:
            return True, "^", count


def Jackpot(ticket: str) -> bool:
    if ("@" * 20) in ticket:
        match_symbol = "@"
        return True, match_symbol
    elif ("#" * 20) in ticket:
        match_symbol = "#"
        return True, match_symbol
    elif ("$" * 20) in ticket:
        match_symbol = "$"
        return True, match_symbol
    elif ("^" * 20) in ticket:
        match_symbol = "^"
        return True, match_symbol
    return False

collection_of_tickets = [ticket.strip() for ticket in input().split(", ")]

for ticket in collection_of_tickets:
    if valid_ticket(ticket):
        if Jackpot(ticket):
            is_jackpot, match_symbol = Jackpot(ticket)
            print(f'ticket "{ticket}" - {10}{match_symbol} Jackpot!')
            continue
        if winning_ticket(ticket):
            is_winning, match_symbol, count = winning_ticket(ticket)
            print(f'ticket "{ticket}" - {count}{match_symbol}')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")