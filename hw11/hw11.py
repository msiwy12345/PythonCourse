import os

path_to_file = [
    r"/home/siwy/python/section2/labs/hw11/s1.py",
    r"/home/siwy/python/section2/labs/hw11/s2.py",
]

for path in path_to_file:
    with open(path, 'r') as file:
        print("File: ", os.path.basename(path))
        source=file.read()
        exec(source)