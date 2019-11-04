
def solve(grid, visit, edge, ans, n_boys, n_girls, i):
    
    if i == n_girls:
        return 0
    
    if edge[i] == 0:
        edge[i] = 1
        
        # Enter the edges
        print("Enter the edge information: ")
        for j in range(n_boys):
            grid[i][j] = int(input())
    
    match = 0
    for j in range(n_boys):
        if grid[i][j] == 1 and visit[j] == 0:
            visit[j] = 1
            temp = 1 + solve(grid, visit, edge, ans, n_boys, n_girls, i+1)
            
            if match < temp:
                match = temp
                ans[i] = j
            visit[j] = 0

    return match

if __name__ == '__main__':
    
    # L-set
    print("Enter number of boys: ")
    n_boys = int(input())
    
    # R-set
    print("Enter number of girls: ")
    n_girls = int(input())
    
    # grid
    grid = []
    for _ in range(n_girls):
        grid.append([0 for _ in range(n_boys)])
    
    # auxillary 
    edge = [0 for _ in range(n_girls)]
    ans = [-1 for _ in range(n_girls)]
    visit = [0 for _ in range(n_boys)]
    
    # solution
    max_match = solve(grid, visit, edge, ans, n_boys, n_girls, 0)
    
    print("Maximum number of matches: ", max_match)
    print(ans)