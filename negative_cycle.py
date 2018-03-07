#Uses python3

import sys


def negative_cycle(adj, cost):
    #print(cost)
    #print(adj)
    #write your code here
    #dist = [(len(adj))*100000000] * len(adj)
    #print(dist)
    #prev = [-1] * len(adj)
    #print(prev)
    total = [n for n in range(len(adj))]
    #print(total)
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
    #dist[s] = 0
    #print(total)
    for i in total:
        for j in cost[i]:
            if j < 1:
                return 1
            #print(j)
    #for vertex in range(len(adj) -1):
    #   print('hello')
        #for edge in 









    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))