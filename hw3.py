import os

def CountWords(path):
    with open(path, 'r', encoding="utf-8") as file:
        content = file.read()
        w_count=len(content.split())
    return w_count

path =r'\\wsl.localhost\Ubuntu\home\siwy\python\section1\hw3.txt'

if os.path.isfile(path):
    print("plik %s istnieje" %path)
else:
    print("tworze plik %s" %path)
    open(path,'x').close()

words=CountWords(path)

print("w pliku jest %s slow" %words)

#os.remove(path)