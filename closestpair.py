import math

def dist(p1, p2):
    
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1])**2)

def closest_split_pair(P_x, P_y, delta, mn_pair):

    ln = len(P_x)
    mid_x = P_x[ln // 2][0]
    
    s_y = [p for p in P_y if mid_x - delta <= p[0] <= mid_x + delta]
    best = delta  
    ln_y = len(s_y)  

    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)

            if dst < best:
                best_pair = p, q
                best = dst

    return best_pair[0], best_pair[1], best

def brute(P_x):

    mi = dist(P_x[0], P_x[1])
    p1 = P_x[0]
    p2 = P_x[1]
    ln = len(P_x)
    
    if ln == 2:
        return p1, p2, mi

    for i in range(ln-1):
        for j in range(i + 1, ln):
            
            if i != 0 and j != 1:
                d = dist(P_x[i], P_x[j])
                
                if d < mi:  
                    mi = d
                    p1, p2 = P_x[i], P_x[j]
    
    return p1, p2, mi


def closest_pair(P_x, P_y):
    
    ln = len(P_y)  
    if ln <= 3:
        return brute(P_x)  
    
    mid = ln // 2  
    Qx = P_x[:mid] # left sublist sorted on the basis of x-axis 
    Rx = P_x[mid:] # right sublist sorted on the basis of y-axis
    
    midpoint = P_x[mid][0]  # x coordinate of the midpoints
    
    Qy = list() # left sublist sorted on the basis of y-axis
    Ry = list() # right sublist sorted on the basis of y-axis

    for p in P_y:  
        if p[0] <= midpoint:
           Qy.append(p)
        else:
           Ry.append(p)

    (p1, q1, d1) = closest_pair(Qx, Qy)
    (p2, q2, d2) = closest_pair(Rx, Ry)
    
    if d1 <= d2:
        d = d1
        mn_pair = (p1, q1)
    else:
        d = d2
        mn_pair = (p2, q2)
    
    (p3, q3, d3) = closest_split_pair(P_x, P_y, d, mn_pair)
    
    if d <= d3:
        return mn_pair[0], mn_pair[1], d
    else:
        return p3, q3, d3


if __name__ == "__main__":
    
    print("Enter the x - coordinates: ")
    x = [int(i) for i in input().split(' ')]

    print("Enter the y - coordinates: ")
    y = [int(i) for i in input().split(' ')]
    
    P = list(zip((x, y)))

    P_x = sorted(P, key=lambda x: x[0])
    P_y = sorted(P, key=lambda x: x[1]) 
    p1, p2, d = closest_pair(P_x, P_y)  
    
    print("Two closest pairs are: ", p1, p2)
    print("Minimum distance: ", d)
    