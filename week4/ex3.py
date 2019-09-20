input_items = [['A', 0.01 , ''], ['B', 0.24, ''], ['C', 0.05, ''],
               ['D', 0.2, ''], ['E', 0.47, ''], ['F', 0.01, ''],
               ['G', 0.02, '']
               ]
result = []
class Node:

    def __init__(self, child1, child2, frq, value):
        self.child1 = child1
        self.child2 = child2
        self.frq = frq
        self.value = value
        if (child1 is None and child2 is None):
            self.isLeaf = False
        else:
            self.isLeaf = True


def huffman(items):
    global result
    nodes = []
    for item in items:
        item[1] = item[1] * 100
    sorted_items = sorted(items, key=get_fr)
    for item in sorted_items:
        nodes.append(Node(None, None, item[1], item[0]))

    while (len(nodes) > 1):
       nodes = [Node(nodes[0], nodes[1], nodes[0].frq + nodes[1].frq, None)] +\
       nodes[2:]
       nodes = sort_nodes(nodes)
    traverse_tree(nodes[0], "")
    print(result)


def traverse_tree(node, codeword):
    global result
    if node.isLeaf:
        result.append((node.value, codeword))
        return
    traverse_tree(node.child1, codeword + '0')
    traverse_tree(node.child2, codeword + '1')

def get_fr(item):
    return item[1]

def sort_nodes(nodes):
    for i in range(len(nodes)):
        for j in range (0, len(nodes) - i -1):
            if nodes[j].frq > nodes[j+1].frq:
                nodes[j].frq, nodes[j+1].frq = nodes[j+1].frq, nodes[j].frq
    return nodes

if __name__ == '__main__':
    huffman(input_items)

