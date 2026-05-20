from collections import deque

graph = {}
graph["Du"] = ["Bob", "Claire", "Alice"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Claire"] = ["Tom", "Jonny"]
graph["Alice"] = ["Peggy"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Jonny"] = []
graph["Tom"] = []

def is_seller(person):
    return person[-1] == 'm'

def search(name):
    queue = deque()
    queue += graph[name] #queue.append(name)
    searched = []
    while queue:
        person = queue.popleft()
        if not person in searched:
            if is_seller(person):
                print(person + " sells mangos")
                return True
            else:
                queue += graph[person]
                searched.append(person)
    return False

print(search("Du"))