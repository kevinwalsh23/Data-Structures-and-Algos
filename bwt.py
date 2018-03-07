# python3
import sys

def rotate(text):

	#create all lines in bwt transformation
    n = len(text)
    newtxt = text * 2
    #print(newtxt)
    for i in range(n):
    	x = newtxt[i:i + n]
    	#print(x)
    return [newtxt[i:i + n] for i in range(n)]


def wheels(text):
	#get all lines in bwt trans, then sort these lines
	y = sorted(rotate(text))
	return(y)
    #return sorted(rotate(text))


def BWT(text):
    
    #print(text)
    n = len(text)
    #print(n)

    wheelburrow = wheels(text)

    #for i in range(n):
    #	return''.join([wheelburrow[i][n-1]])
    #return last letter of each line and join into string
    return ''.join([wheelburrow[i][n - 1] for i in range(n)])

    return ""

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))