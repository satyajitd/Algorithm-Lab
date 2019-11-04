def findMedian(ar, l, n):
    ar[l:l+n].sort()
    return ar[l+int(n/2)]

def partition(ar, l, r, x):
    i = l
    while(i < r):
        if(ar[i] == x):
            break
        i = i + 1
    
    t = ar[r]
    ar[r] = ar[i]
    ar[i] = t

    i = l - 1
    j = l
    while(j < r):
        if ar[j] <= x:
            i = i + 1
            t = ar[j]
            ar[j] = ar[i]
            ar[i] = t
        j = j + 1
        
    i = i + 1
    t =  ar[r]
    ar[r] = ar[i]
    ar[i] = t

    return i

def kthSmallest(ar, l, r, k):
    if(k > 0 and k <= r-l+1):
        n = r - l + 1
        median = []
        i = 0 
        groups = int(n/5)
        while i < groups:
            median.append(findMedian(ar, l + i*5, 5))
            i = i + 1
        if i*5 < n:
            median.append(findMedian(ar, l + i*5, n%5))
            i = i + 1
        
        if i == 1:
            medOfmed = median[i-1]
        else:
            medOfmed = kthSmallest(median, 0, i-1, int(i/2))
        
        pos = partition(ar, l, r, medOfmed)

        if pos - l == k - 1:
            return ar[pos+1]
        elif pos - l > k - 1:
            return kthSmallest(ar, l, pos-1, k)
        else:
            return kthSmallest(ar, pos+1, r, k-pos+l-1)

if __name__ == "__main__":
    N = int(input("Enter the number of oil wells: "))
    
    #X = [int(x) for x in input("Enter the x-coordinates for {} wells: ".format(N)).strip().split()]
    Y = [int(x) for x in input("Enter the x-coordinates for {} wells: ".format(N)).strip().split()]

    y_min = min(Y)

    print("Median of the list : ", kthSmallest(Y, 0, len(Y)-1, int(len(Y)/2)))