def merge(left, right):
    count = 0
    merged = []
    
    i = 0; j = 0
    N = len(left); M = len(right)
    
    while(i < N and j < M):
        if left[i] <= right[j]:
            merged.append(left[i])
            i = i + 1
        else:
            count += N - i
            merged.append(right[j])
            j = j + 1 
    
    while(i < N):
        merged.append(left[i])
        i = i + 1 
    while(j < M):
        merged.append(right[j])
        j = j + 1
    
    return merged, count

def sort_and_count(array):
    if len(array) == 1:
        return array, 0

    left = array[0:int(len(array)/2)]
    right = array[int(len(array)/2):len(array)]
    
    sorted_left, left_count = sort_and_count(left)
    sorted_right, right_count = sort_and_count(right)
    merged, count = merge(sorted_left, sorted_right)
    
    return merged, (left_count + right_count + count)

'''
If we have N movies then the rating ranges from 1 to N, which converted into the range of 0 to N - 1.
For the simplicity, it is assumed that the ratings are distinct.
'''

if __name__ == '__main__':
    
    N = int(input("Enter the number of movies: "))
    M = int(input("Enter the size of the database: "))
    
    db = {}
    print("\nEnter the database: \n")
    
    for _ in range(M):
        key = input("Enter the name of the person: ")
        print("Rating for %d movies: ", N)
        db[key] = [int(x) - 1  for x in input().strip().split()]
        print("\n")

    print("Your rating for %d movies: ", N)
    yourRatings = [int(x) - 1 for x in input().strip().split()]
    
    inversionCount = {}
    array = [0 for _ in range(N)]

    for key, values in db.items():
        '''
            db_Rating:  5 4 2 3 1   <= index
            yourRating: 4 3 2 1 5   <= values
            Then,
            array[5] = 4
            array[4] = 3 
        '''
        for i in range(N):
            array[values[i]] = yourRatings[i]

        sortedArray, count = sort_and_count(array)
        inversionCount[key] = count
        
    print("\nComparsion the ratings in terms of inversion count: ")
    print(inversionCount)
    