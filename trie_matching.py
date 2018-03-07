# python3
import sys

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    index = 1

    for thing in patterns:
        currentnode = tree[0]
        for alpha in thing:
            if alpha in currentnode.keys():
                currentnode = tree[currentnode[alpha]]
            else:
                currentnode[alpha] = index
                tree[index] = {}
                currentnode = tree[index]
                index = index + 1
    return tree

def solve (text, n, patterns):
    result = []
    trie = build_trie(patterns)

    n = len(text)
    for i in range(n):
        if prefix_trie_matching(text[i:], trie):
            result.append(i)

    return result

def prefix_trie_matching(text, trie):
    idz = 0
    sym = text[idz]
    currentnode = trie[0]
    
    while True:
        if not currentnode:
            return True
        elif sym in currentnode.keys():
            currentnode = trie[currentnode[sym]]
            idz = idz + 1
            if idz < len(text):
                sym = text[idz]
            else:
                sym = '@'
        else:
            return False

if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]

    ans = solve(text, n, patterns)
    sys.stdout.write(' '.join (map(str, ans)) + '\n')
