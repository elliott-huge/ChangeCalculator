# REQUIREMENTS:
# Function takes desired change, and a list of available coins
# Function checks whether it is able to provide the exact change from the available coins
# Returns the string "INSUFFICIENT COINS" if unable
# Returns "SUFFICIENT COINS" and prints the coin combination if able
from itertools import repeat
def exactChange(target_change: float, available_coins: list):
    available_coins.sort(key = lambda coin: coin[0], reverse = True)

    # float -> int
    available_pennies = [[int(d[0] * 100), int(d[1] * 100)] for d in available_coins]
    target_change_pennies = int(target_change*100)

    # setup to enumerate every individual coin
    available_pennies_long = []
    coinCount = lambda entry : int(entry[1]/entry[0])

    for denom in available_pennies:
        available_pennies_long.extend(repeat(denom[0], coinCount(denom)))
    
    change = _getChangeRecursive(target_change_pennies, available_pennies_long)
    if change == False:
        return "INSUFFICIENT COINS"
    else:
        print(change)
        return "SUFFICIENT COINS"

def _getTotalCash(available_coins: list) -> float:
    cash = 0
    for denomination in available_coins:
        cash += denomination[0] * denomination[1]
    return cash / 100


def _getChangeRecursive(due, available_coins):
    for coin in available_coins:
        remainder = due - coin

        if remainder == 0:
            return [coin]
        
        elif remainder > 0:
            current_coins = available_coins.copy()
            current_coins.remove(coin)
            result = _getChangeRecursive(remainder, current_coins)
            if result != False:
                result.append(coin)
                return result
        else:
            continue

    return False