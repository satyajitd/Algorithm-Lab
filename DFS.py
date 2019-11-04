import pprint

def DFS(grid, i, j, color, new_color, visit, dirc):
    if(visit[i][j] == 0 and grid[i][j] == color):
        visit[i][j] = 1
        grid[i][j] = new_color
        for x, y in dirc:
            if i+x >= 0 and i+x < len(visit) and j+y >= 0 and j+y < len(visit):
                DFS(grid, i+x, j+y, color, new_color, visit, dirc)

def create_visit(siz):
    grid = []
    for _ in range(siz):
        grid.append([0 for _ in range(siz)])
    return grid

if __name__ == "__main__":
    
    print("Size of the grid: ")
    siz = int(input())
    grid = []
    print("Enter the grid: ")
    for _ in range(siz):
        grid.append(list(input().strip().split(' ')))
    
    print("Start node: ")
    i, j = input().strip().split(' ')
    i = int(i)
    j = int(j)
    print("Change to: ")
    color = input()

    dirc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visit = create_visit(siz)

    DFS(grid, i, j, grid[i][j], color, visit, dirc)
    pprint.pprint(grid)