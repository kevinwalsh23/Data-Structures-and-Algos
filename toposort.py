#Uses python3
import sys


#


def dfs(adj, used, order, x):
    #write your code here
    for x in adj:
        print(x)
        #print(used[i])
        if used[i] != 1:
            #print(i)
            explore(x, used)
            if i:
                order.append(x)
                #order.append(adj.index(i))
            else:
                #order.append(i)
                order.append(adj.index(x))
            #print(str(i) + 'two')
        #if not i:
        #    print('hello')

    #print(used)
    #order = used
    return(order, used)

    #print(adj)
    pass

def explore(v, used):
    #used = [0] * len(adj)
    used[v] = 1
    for j in adj[v]:
        if used[j] != 1:
            explore(j)
    print(v)

    #order.append(v)
    #print(v)
    #print(adj[v])
    #print(postvisit(v, used))
    return v
    #return order

def postvisit(v, used):
    used[v] == clock
    clock += 1

def toposort(adj):
    print(adj)
    used = [0] * len(adj)
    #print(used)
    order = []

    for i in range(len(adj)):
        print(i)
        dfs(adj, used, order, i)


    #print(used)
    order = used
    return order

#used = [0] * len(adj)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

