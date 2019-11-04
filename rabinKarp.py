#hwtq-icbg
if __name__ == "__main__":
    d = 256 #no. of input characters
    q = 101
    
    text = input("Enter the text: ").strip()
    pattern = input("Enter the pattern: ").strip()

    m = len(pattern)
    n = len(text)

    if(m > n):
        print("Can't find the pattern")
        exit()

    h = 1 # it will store d^(m-1)
    t = 0 # hash for the text[i:i+m+1](len m)
    p = 0 # hash for the pattern

    for _ in range(m - 1):
        h = (h * d) % q
    
    for i in range(m):
        t = (t * d + ord(text[i])) % q
        p = (p * d + ord(pattern[i])) % q

    for i in range(0, n - m + 1):
        if(p == t):
            k = 0
            flag = True
            for j in range(i, i + m):
                if(pattern[k] != text[j]):
                    flag = False
                    break
                k = k + 1
            if(flag):
                print("The pattern found is at ", i)
        if(i < n - m):
            t = (d * (t - ord(text[i])*h) + ord(text[i + m])) % q
            if(t < 0):
                t = t + q