#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    #print(patterns)
    #print(tree)
    index = 1

    for pattern in patterns:
    	currentnode = tree[0]

    	for alpha in pattern:
    		if alpha in currentnode.keys():
    			currentnode = tree[currentnode[alpha]]
    		else:
    			currentnode[alpha] = index
    			tree[index] = {}
    			currentnode = tree[index]
    			index += 1
    #return tree
    			#alpha in tree[currentnode[alpha]]
    			#urrentsymbol = pattern[alpha]
    # write your code here
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().splitq	``()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
