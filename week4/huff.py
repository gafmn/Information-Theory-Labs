from collections import Counter
class Node():
    def __init__(self, child1, child2, letter, weight):
        self.ch1 = child1
        self.ch2 = child2
        if (child1!=None and child2!=None):
            self.weight = child1.weight + child2.weight
            self.is_leaf = False
        else:
            self.is_leaf = True
            self.letter = letter
            self.weight = weight

def sort_in_reverse(nodes):
    n = len(nodes)
    for i in range(n):
        for j in range(0, n-i-1):
            if nodes[j].weight > nodes[j+1].weight :
                nodes[j], nodes[j+1] = nodes[j+1], nodes[j]
def reverse_tree(node, codeword):
    global glob_res
    if node.is_leaf:
        glob_res.append((node.letter, codeword))
        return
    reverse_tree(node.ch1, codeword + '0')
    reverse_tree(node.ch2, codeword + '1')

my_str = "a"*10 + "b"*20 + "c"*10 + "d"*40 +  "e"*20
init_sum = len(my_str)
counts = Counter(my_str)
counts = counts.most_common()[::-1]
glob_res = []
node_list = []
for i in range(len(counts)):
    node_list.append(Node(None, None, counts[i][0], counts[i][1]))
while (len(node_list) > 1):
    node_list = [Node(node_list[0], node_list[1], None, None)] + node_list[2:]
    sort_in_reverse(node_list)
if node_list[0].is_leaf:
    glob.res.append((counts[0][0], '0'))
else:
    reverse_tree(node_list[0].ch1, '0')
    reverse_tree(node_list[0].ch2, '1')
print(glob_res)

