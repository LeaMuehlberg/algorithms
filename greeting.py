tree = {
    'H': ['A', 'O'],
    'A': ['L', 'L'],
    'L': [], 'L': [], 'O':[]
}

def tiefensuche(tree, node, visited = None):
    if visited is None:
        visited = set()
    
    print(node)
    visited.add(node)
    
    for child in tree[node]:
        if child is not visited:
            tiefensuche(tree, child, visited)

tiefensuche(tree, 'H')