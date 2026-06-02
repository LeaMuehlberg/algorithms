from collections import deque

# breitensuche: queue, mango seller. kürzesten weg finden / existiert ein weg
breiten_tree = {}
breiten_tree["Du"] = ["Bob", "Claire", "Alice"]
breiten_tree["Bob"] = ["Anuj", "Peggy"]
breiten_tree["Anuj"] = []
breiten_tree["Peggy"] = []
breiten_tree["Claire"] = ["Tom", "Jonny"]
breiten_tree["Tom"] = []
breiten_tree["Jonny"] = []
breiten_tree["Alice"] = ["Peggy"]

def is_seller(node):
    return node[-1] == 'm'

def breiten_search(node):
    queue = deque()
    queue += breiten_tree[node]
    visited = []
    while queue:
        child = queue.popleft()
        if child is not visited:
            if is_seller(child):
                print(child + " sells.")
                return True
            else:
                queue += breiten_tree[child]
                visited.append(child)
    return False

print(breiten_search("Du"))

# tiefensuche: alle nodes im tree durchlaufen, hallo
tiefen_tree = {
    'H': ['A', 'O'],
    'A': ['L', 'L'],
    'L': [], 'O': []
}
def tiefen_search(tree, node, visited = None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)
    
    for child in tree[node]:
        if child is not visited:
            tiefen_search(tree, child, visited)
            
tiefen_search(tiefen_tree, 'H')

# dijkstra: tree, costs, parents. schnellsten weg finden
tree = {}
tree["start"] = {} # tree["start"].keys()
tree["a"] = {}
tree["b"] = {}
tree["fin"] = {}
tree["start"]["a"] = 6
tree["start"]["b"] = 2
tree["a"]["fin"] = 1
tree["b"]["a"] = 3
tree["b"]["fin"] = 5

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

visited = []

def lowest_cost_node(costs): # sowie bei selectionsort zuerst das kleinste elem finden
    # default werte weil wir noch keine ahnung haben 
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node] # costs["a"] = 6
        if cost < lowest_cost and node not in visited:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
    
node = lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = tree[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    visited.append(node)
    node = lowest_cost_node(costs)

# zum printen
parents["start"] = None
path = []
node = "fin"
while node is not None:
    path.append(node)
    node = parents[node]
path.reverse()
print(path)

# selection sort: das größte/kleinste elem finden -> in neue liste packen
def get_smallest(list):
    if len(list) == 1:
        return list[0]
    temp_min = get_smallest(list[1:])
    return list[0] if list[0] < temp_min else temp_min

def selection_sort(list):
    new_list = []
    for i in range(len(list)):
        smallest = get_smallest(list)
        list.pop(list.index(smallest)) # man braucht den index zum poppen
        new_list.append(smallest)
    return new_list
        
print(selection_sort([34, 2, 14]))

# quick sort: pivot elem
def quicksort(list):
    if len(list) < 2:
        return list
    pivot = list[0]
    min_list = [i for i in list[1:] if i <= pivot]
    max_list = [i for i in list[1:] if i > pivot]
    return quicksort(min_list) + [pivot] + quicksort(max_list)
print(quicksort([4, 56, 3, 19]))