# Cashier's Algo will fail for example:
# denominations : 1 5 6 9
# money: 11


if __name__ == "__main__":
    print("Enter the coin denominations: ")
    denominations = [int(x) for x in input().strip().split(' ')]
    denominations.sort(reverse=True)

    print("Enter the amount: ")
    money = int(input())

    coins = 0
    for i in denominations:
        coins = coins + money//i
        money = money%i
    
    print("Required Coins : ", coins)