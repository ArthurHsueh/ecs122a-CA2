import time
start_time = time.time()

def compute_diamter(n, edges):
    # Input: `n` - the size of the tree
    # `edges` - a list of pairs of integers denoting ends of edges of the tree
    # Output: An integer - the diameter of the tree
    diameter = 0
    node = edges[0][0]

    for i in range(2):
        dist = [0 for i in range(n+1)]
        layer = [[] for i in range(n+1)]
        adj = [[] for i in range(n+1)]
        marked = [False for i in range(n+1)]

        dist[node] = 0
        layer[0].append(node)
        for e in edges :
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        marked[node] = True

        for l in range(n):
            for u in layer[l]:
                for w in adj[u]:
                    if marked[w] == False:
                        marked[w] = True
                        dist[w] = l + 1
                        layer[l+1].append(w)

        for i in range(n, 0, -1):
            if layer[i]:
                diameter = i
                node = layer[i][0]
                break
    return diameter


T = int(input())
for _ in range(T):
    n = int(input())
    edges = []
    for e in range(n-1):
        u, v  = map(int, input().split(' '))
        edges.append((u, v))
    print(compute_diamter(n, edges))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")
