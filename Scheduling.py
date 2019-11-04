def sortSecond(val):
    return val[1]

if __name__ == "__main__":
    print("Enter the number of the jobs: ")
    n = int(input())

    jobs = []
    ans = 1
    for _ in range(n):
        print("Enter start and finish times: ")
        temp = [int(x) for x in input().strip().split(' ')]
        jobs.append(temp)

    j = 0
    jobs.sort(key = sortSecond)
    for i in range(1, n):
        if(jobs[i][0] >= jobs[j][1]):
            ans = ans + 1
            j = i    

    print("Max jobs that can scheduled: ", ans)