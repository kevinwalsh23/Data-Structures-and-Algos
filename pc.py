#Uses python3
import sys
import math

def distance(xi, yi, xj, yj):
    return math.sqrt(math.pow(xi-xj, 2) + math.pow(yi-yj, 2))

def minimum_distance(vertices, adj, weight):
    result = 0.
    Z = set();
    Z.add(0)

    while len(Z) != vertices:
        crossing = set()
        for u in Z:
            for v in adj[u]:
                if v not in Z:
                    crossing.add((u, v))
        side = sorted(crossing, key=lambda e: weight[e[0]][e[1]])[0]
        result += weight[side[0]][side[1]]
        Z.add(side[1])

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    adj = [[] for _ in range(n)]
    weight = [[0]*n for _ in range(n)]
    for i in range(n):
        adj[i] = list(v for v in range(n) if v != i)
        for j in range(n):
            if i != j:
                w = distance(x[i], y[i], x[j], y[j])
                weight[i][j] = w
                weight[j][i] = w

    print("{0:.9f}".format(minimum_distance(n, adj, weight)))