tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}

def tiefensuche(tree, node, visited = None):
    if visited is None:
        visited = set() #init
    
    visited.add(node) #node = knoten
    print(node)
    
    for child in tree[node]:
        if child not in visited:
            tiefensuche(tree, child, visited)
            
tiefensuche(tree, 'A')