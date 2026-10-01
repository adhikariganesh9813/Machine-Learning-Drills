from os import listdir
from os.path import isfile, join
from collections import deque

def printnames(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            full_path = join(dir, file)
            if isfile(full_path):
                print(full_path)
            else:
                search_queue.append(full_path)

printnames('.')

print("\n")

def printnames_recursive(dir):
    for file in sorted(listdir(dir)):
        full_path = join(dir, file)
        if isfile(full_path):
            print(full_path)
        else:
            printnames_recursive(full_path)

printnames_recursive('.')
