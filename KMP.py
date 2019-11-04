def LPS(pattern):
    m = len(pattern)
    lps = [0 for _ in range(m)]
    j = 0
    i = 1
    while(i < m):
        if(pattern[j] == pattern[i]):
            lps[i] = j + 1
            i = i + 1
            j = j + 1
        else:
            if(j == 0):
                lps[i] = 0
                i = i + 1
            else:
                j = lps[j - 1]
    return lps 

def KMP(text, pattern):
    m = len(pattern)
    n = len(text)

    lps = LPS(pattern)
    i=0
    j=0
    while(i < n and j < m):
        if(text[i] == pattern[j]):
            i = i + 1
            j = j + 1
        else:
            if(j != 0):
                j = lps[j-1]
            else:
                i = i + 1

    if(j == m):
        return True
    return False

if __name__ == "__main__":
    text = input("Enter the text: ").strip()
    pattern = input("Enter the pattern: ").strip()
    
    if(KMP(text, pattern)):
        print("The pattern is present in the text.")
    else:
        print("The pattern is not present in the text.")