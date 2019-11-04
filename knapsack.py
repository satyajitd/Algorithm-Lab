if __name__ == "__main__":
    print("Enter the total weight of the bag: ")
    W = int(input())

    print("Enter the no.of items given to us: ")
    N = int(input())

    print("\nEnter the weight and value of the items: " )

    items = []
    for i in range(1, N+1):
        print("\nEnter the weight of the item ", i, " : ")
        w = int(input())
        print("Enter the value of the item ", i, " : ")
        v = int(input())
        items.append([v//w, v, w])
    
    items.sort(reverse=True)

    max_value = 0
    for r, v, w in items:
        if(w <= W):
            max_value += v
            W -= w
        else:
            frac = W / w
            max_value += frac * v 
            W = int(W - frac * w)
            break

    print("\nMax value that can be obtained in Fractional Knapsack: ", max_value)