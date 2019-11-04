from random import randint
import matplotlib.pyplot as plt

def fracKnapSack(weights, values, N, W):
    items = []
    for i in range(N):
        items.append([values[i]//weights[i], values[i], weights[i]])
    
    items.sort(reverse=True)
    
    max_value = 0
    for _, v, w in items:
        if(w <= W):
            max_value += v
            W -= w
        else:
            frac = W / w
            max_value += frac * v 
            W = int(W - frac * w)
            break
    
    return max_value

def randKnapSack(weights, values, N, W):
    value = 0

    while(W > 0 and N > 0):
        if(N == 1):
            i = 0
        else:    
            i = randint(0, N-1)
        
        if(weights[i] <= W):
            value += values[i]
            W -= weights[i]

        else:
            frac = W / weights[i]
            value += frac * values[i] 
            W = int(W - frac * weights[i])
            break

        del values[i]
        del weights[i]
        N = N - 1

    return value

if __name__ == "__main__":
    
    N = [7]
    fracVal = []
    randVal = []
    for n in N:
        W = int(input("Enter the total capacity: "))

        print("Enter the weight of the items: ")
        weights = [int(x) for x in input().strip().split()]
        print("Enter the value of the items: ")
        values = [int(x) for x in input().strip().split()]
        
        fracVal.append(fracKnapSack(weights, values, n, W))
        randVal.append(randKnapSack(weights, values, n, W)) 
        
        print(fracVal)
        print(randVal)

    plt.scatter(N, fracVal, color = "blue", label = "fractional Knapsack")
    plt.scatter(N, randVal, color = "red", label = "random Knapsack")

    plt.xlabel('No. of items')
    plt.ylabel('Value obtained')
    plt.legend()

    plt.show()
