def isBipartite(src, nodes, color, graph):
    color[src] = 1
    queue = []
    queue.append(src)

    while queue: 
        u = queue.pop() 

        if graph[u][u] == 1: 
            return False

        for v in range(nodes): 

            if graph[u][v] == 1 and color[v] == -1: 
                color[v] = 1 - color[u] 
                queue.append(v) 

            elif graph[u][v] == 1 and color[v] == color[u]: 
                return False

    return True

if __name__ == "__main__":
    
    print("Number of Nodes: ")
    nodes = int(input())
    
    print("Enter the adjacency matrix: ")
    
    graph = []
    for _ in range(nodes):
        graph.append([int(x) for x in input().strip().split(' ')])
    
    color = [-1] * nodes
    print("Enter the source node (0-indexed): ")
    src = int(input())

    if isBipartite(src, nodes, color, graph):
        print("Partition of vertices: ")
        print(color)
    else :
        print("Not a bipartite graph")