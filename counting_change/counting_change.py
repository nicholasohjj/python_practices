# Program returns number of possibilities on counting change of coins with a given amount of money, and types of coins.
list = [1, 5, 10, 20, 50] # given 1, 5, 10, 20 50 cents

def denomination(n):
    return list[n-1]

def counting_change(amount, types):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif types == 0:
        return 0
    else:
        return counting_change(amount-denomination(types), types) + counting_change(amount,types-1)
    

print(counting_change(100,5))