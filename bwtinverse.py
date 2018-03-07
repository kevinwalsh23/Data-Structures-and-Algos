# python3
import sys

def InverseBWT(bwt):
    # write your code here
    lastly = [(value, idz)  for (idz, value) in enumerate(bwt)]
    #print(lastly)
    uno = sorted(lastly)
    #print(uno)

    uno_to_lastly = {f: l for f, l in zip(uno, lastly)}

    #print(uno_to_last)
    
    next = uno[0]
    result = ''
    for i in range(len(bwt)):
        result += next[0]
        next = uno_to_lastly[next]

    return result[::-1]

    print(x)
    return ""


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))