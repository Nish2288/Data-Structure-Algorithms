'''
We will be given an array of positive integers, which represent the values of coins that we have in our possession.
The array could have duplicates. We are asked to write a function that returns the minimum amount of change that we cannot create with our coins. For instance,
if the input array is [1, 2, 5], the minimum amount of change that we cannot create is 4, since we can create 1, 2, 3 (1 + 2) and 5.

Time Complexity: O(nlogn)
'''

def nonConstructibleChange(coins):
    currentChange = 0
    coins.sort()

    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1

        currentChange += coin
    return 1

coins = [5, 7, 1, 1, 2, 3, 22]

print(nonConstructibleChange(coins))