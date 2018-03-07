#Uses python3

import sys


def acyclic(adj):
    #print(adj)
    """
    visited= []
    queue = [n for n in range(len(adj))] 

    while(queue):
        c = queue.pop(0)

        if(c in visited):
            return 1
        
        visited.append(c)
        nodes = adj[c]
        if(nodes == []):
            visited = []
        else:   
            queue = nodes + queue
    """

    #print(adj)
    
    total = [n for n in range(len(adj))]
    print(total)
    curr = 0

    while(curr != len(total)):
        curr = len(total)
        edges =[]

        for n in total:
            edges += adj[n]

        edges = list(set(edges))
        #print("edges", edges)
        #print("total", total)
        remove = -1
        for i in total:
            if(i not in edges):
                remove = i
                break

        if remove != -1:
            total.pop(total.index(i))

    #print(total)

    if(len(total) > 0):
        return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
