
#----------------------------
# Функція жадібного алгоритму
#----------------------------

def find_coins_greedy(coins_sum, coins):
  coins_dict = {}

  for coin in coins:
    if coins_sum >= coin:
      count = coins_sum // coin
      coins_dict[coin] = count
      coins_sum -= coin * count

  return coins_dict
      


#----------------------------------
# Функція динамічного програмування
#----------------------------------

def find_min_coins(coins_sum, coins):
  dp = [float('inf')] * (coins_sum + 1)
  dp[0] = 0
  
  for coin in coins:
    for i in range(coin, coins_sum + 1):
      dp[i] = min(dp[i], dp[i - coin] + 1)
  
  if dp[coins_sum] == float('inf'):
    return {}
  
  result = {}
  
  while coins_sum > 0:
    for coin in coins:
      if coins_sum - coin >= 0 and dp[coins_sum] == dp[coins_sum - coin] + 1:
        result[coin] = result.get(coin, 0) + 1
        coins_sum -= coin
        break

  return result


#------------
# Test
#------------

coins = [50, 25, 10, 5, 2, 1]

print(find_coins_greedy(976, coins))
print(find_min_coins(976, coins))
