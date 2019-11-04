import collections
 
class Graph:
 
    def __init__(self, graph):
        self.graph = graph 
        self.ROW = len(graph)
 
    def BFS(self, s, t, parent):
 
        visited = [False] * (self.ROW)
 
        queue = collections.deque() 
        queue.append(s)
        visited[s] = True
 
        while queue:
            u = queue.popleft()
 
            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
 
        return visited[t]
 
    def EdmondsKarp(self, source, sink):
 
        parent = [-1] * (self.ROW)
        max_flow = 0 
 
        while self.BFS(source, sink, parent):
 
            path_flow = float("Inf")
            t = sink
            while t != source:
                path_flow = min(path_flow, self.graph[parent[t]][t])
                t = parent[t]
 
            max_flow += path_flow
 
            v = sink
            while v !=  source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
 
if __name__ == "__main__":
 
    print("Enter the no. of vertices of the graph: ")
    n_v = int(input())
 
    print("Enter the graph as adjacency matrix: ")
    adj = []
    for _ in range(n_v):
        adj.append([int(x) for x in input().strip().split(' ')])
 
    graph = Graph(adj)
    print("Enter the source node and sink node: ")
    s, t = map(int, input().strip().split(' '))
 
    print("The maximum flow of the given graph is ", graph.EdmondsKarp(s, t))