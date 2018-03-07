#Uses python3
import sys
import math
import heapq

#PRIM's Algorithm


#sqrt = x**(1/2.0)
#sqr = x**2



def find_distance(x, y):
	edges = []
	for i in range(len(x)):
		for k in range(len(x)):
			dist = math.sqrt(((x[i] - x[k]) ** 2) + ((y[i] - y[k]) **2))
			if dist != 0:
				heapq.heappush(edges, [dist, i, k])
				#edges.append([dist, i, k])
	return edges
	#print(x, y)

def minimum_distance(x, y):
    result = 0.
    for i in x:
    	#print(x, y)
    	edges = find_distance(x,y)
    	#for thing in edges:
    		#print(thing)
    #for m in edges:
    #	if edges[2] == 0:
    #		edges.delete(m)
 
    cost = [1000000000] * len(x)
    #print(dist)
    parent = [-1] * len(x)
    #print(prev)

    cost[0] = 0
    #print(cost)
    #print(edges)
    H = []

    for i in range(len(cost)):
    	heapq.heappush(H, (i, cost[i]))
    #heapq.heappush(H, (0, cost[0]))
    stuff = []
    #print(H)
    #for thing in range(len(x)):
    while H:
    	
    		#print(H)
    	q = []
    	for j in H:
    		q.append(j[0])
    	#print(q)
    	print(H)
    	print('hello')
    	#print(H[0])
    	#for q in H:
    		#print((q[0]))
    	#print(H(0))
    	print(cost)
    	v = heapq.heappop(H)[0]
    	print(v)
    	#print(v)
    	#for z in edges:
    	#	if z[1] == v:
    	#		noob = z[2]
    	#		print(noob)
    	#		#print(H)
    	#		print(cost[noob])
    	#		#for q in H:
    	#		print((q[0]))
    	#		if (cost[noob] > z[0]) and (z[2] in q):
    	#			cost[noob] = z[0]
    	#			parent[noob] = z[1]
    	#			heapq.heappush(H, (z[1], cost[noob]))
    	for z in range(len(edges)):
    		if v not in parent:
    			if edges[z][1] == v:
    				noob = edges[z][2]
    				print(noob)
    			#print(H)
    			#print(cost[noob])
    			#for q in H:
    			#print((q[0]))
    				if (cost[noob] > edges[z][0]) and (noob in q):
    					cost[noob] = edges[z][0]
    					parent[noob] = edges[z][1]
    					heapq.heappush(H, (edges[z][2], cost[noob]))

    				#print(H)




    			#if noob in H:
    		#		print(noob)
    		#print(v) and z[2] in q[0]
    			#print('z')


    		#if edges[z][1] == v or edges[z][2] == v:
    		#	print(z)
			#print(i)
			#print(i)
    		#print(edges[v])
    		#total.append(v)

    		#for 
    	#print(x)
    	#print(len(cost))

    	#return(sum(total))
    		#for n in range(len(cost)):

    			#print(n)
    			#if n != v:
    				#print(n)
    				#print('n')
    			#print(n)
    			#print(H)
    				#if H:
    				#print('hello')

    			#else:
    					#if n in H[0]:
    						#print(n)

    				#print(n[0])
    						#print(cost[n])


    				#print('hello')
    						#thing = cost[n]
    				#print(thing)

				#sqrt = x**(1/2.0)
				#sqr = x**2
				#thing = ((((x[v] - x[n]) **2) + ( (y[v] - y[n])**2)) **(1/2.0))
				#print(thing) 
				#if H[n]:
				#	print(n)   			
    						#if n in H[0] and (cost[n] > ((((x[n] - x[v]) **2) + ( (y[n] - y[v])**2)) **(1/2.0))):
    							#cost[n] = ((((x[n] - x[v]) **2) + ( (y[n] - y[v])**2)) **(1/2.0))
    							#print(cost[n])
    							#cost[n] = min(edges[n][2])
    							#parent[n] = v
    							#heapq.heappush(H, (n, cost[n]))
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

