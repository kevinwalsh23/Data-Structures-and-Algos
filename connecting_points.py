#Uses python3
import sys
import math
import heapq


#sqrt = x**(1/2.0)
#sqr = x**2

#Kruskal's Algorithm


def find_distance(x, y):
	edges = []
	for i in range(len(x)):
		for k in range(len(x)):
			dist = math.sqrt(((x[i] - x[k]) ** 2) + ((y[i] - y[k]) **2))
			if dist != 0:
				heapq.heappush(edges, [dist, i, k])
	return edges
	#print(x, y)

def minimum_distance(x, y):
    result = 0.
    for i in x:
    	#print(x, y)
    	edges = find_distance(x,y)
    	#for thing in edges:
    		#print(thing)
    for m in edges:
    	if edges[2] == 0:
    		edges.delete(m)
    print(edges)

    #print(x)
    #print(y)
    #write your code here
    ##asdf = sorted(edges[0])

   # print(asdf)
    #print('hello')

    group = []
    total = []
    visited = []
    right = []
    left = []
    #for e in (range(len(x) - 1)):
    while len(total) < (len(x)):
    	edge = heapq.heappop(edges)
    	print(edge)
    	if len(total) == 0:
    		total.append(edge[0])
    		left.append(edge[1])
    		right.append(edge[2])
    		print(edge)

    	else:
    			#if edge[1] not in visited or edge[2] not in visited:

    			if edge[1] not in left or edge[2] not in right:

    				if edge[1] in left or edge[1] in right or edge[2] in left or edge[2] in right:
#
    					total.append(edge[0])
    					left.append(edge[1])
    					right.append(edge[2])

    #			print(edge)
    		#total.append(edge)
    	#edge = min(edges)
    	#print(edge)
    #print(total)
    return(sum(total))



    
    
    print(cost)
    result = sum(cost)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
