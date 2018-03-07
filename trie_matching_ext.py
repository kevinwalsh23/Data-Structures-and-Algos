# python3
import sys

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    index = 1

    for pattern in patterns:
        currentnode = tree[0]
        for alpha in pattern:
            if alpha in currentnode:
                currentnode = tree[currentnode[alpha]]
            else:
                currentnode[alpha] = index
                tree[index] = {}
                currentnode = tree[index]
                index = index + 1
        currentnode['$'] = {}
    return tree

def prefix_trie_matching(text, trie, external_idz):
    idz = 0
    symbol = text[idz]
    currentnode = trie[0]
    ress = -1
    
    while True:
        if not currentnode:
            return ress
        if '$' in currentnode:
            return ress
        if symbol in currentnode:
            currentnode = trie[currentnode[symbol]]
            ress = external_idz
            idz += 1
            if idz < len(text):
                symbol = text[idz]
            elif '$' in currentnode:
                return ress
            else:
                symbol = '@'
                ress = -1
        else:
            return ress if '$' in currentnode else -1

def solve (text, n, patterns):
    result = set()
    trie = build_trie(patterns)
    n = len(text)
    for i in range(n):
        val = prefix_trie_matching(text[i:], trie, i)
        if val != -1:
            result.add(val)

    return sorted(list(result))


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
	patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')