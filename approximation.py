import heapq

if __name__ == "__main__":

    print("Enter no. of jobs: ")
    n = int(input())

    print("Enter no. of machines: ")
    m = int(input())    

    load = [0 for i in range(m)] # initially, load in the machines will be zero
    jobs = []

    print("Enter time duration of jobs: ")
    for _ in range(n):
        jobs.append(int(input()))

    jobs.sort(reverse=True)

    for i in range(n):
        heapq.heapify(load)
        load[0] += jobs[i]

    make_span = load[0]
    for i in range(1, len(load)):
        make_span = max(make_span, load[i])

    print("Maximum make span of the machines: ", make_span)