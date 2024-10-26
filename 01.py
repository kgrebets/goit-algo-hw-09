def find_coins_greedy(amount, coins):
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

def find_min_coins(amount, coins):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  

    coin_used = [0] * (amount + 1)

    for coin in coins:
        for sub_amount in range(coin, amount + 1):
            if min_coins[sub_amount - coin] + 1 < min_coins[sub_amount]:
                min_coins[sub_amount] = min_coins[sub_amount - coin] + 1
                coin_used[sub_amount] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    return result


coins=[50, 25, 10, 5, 2, 1]

print(find_coins_greedy(113, coins))
print(find_min_coins(113, coins))
