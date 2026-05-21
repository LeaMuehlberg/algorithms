from os import listdir
from os import isfile, join
from collections import deque

def print_names(start_dir):
    queue = deque()
    queue.append(start_dir)
    while queue:
        dir = queue.popleft()
        for file in sorted(listdir(dir)):
            path = join(dir, file)
            if isfile(path):
                print(file)
            else:
                queue.append(path)

# rekursiv für tiefensuche
def print(start_dir):
    for file in sorted(listdir(dir)):
        path = join(dir , file)
        if isfile(path):
            print(file)
        else:
            print(path)