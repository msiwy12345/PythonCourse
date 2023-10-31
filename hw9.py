ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connection = ((a,b) for a in ports for b in ports)
x=0
while True:
    try:
        print(next(connection))
        x=x+1
    except StopIteration:
        break
print(x)

connection = ((a,b) for a in ports for b in ports if a!=b)
x=0
while True:
    try:
        print(next(connection))
        x=x+1
    except StopIteration:
        break
print(x)

connection = ((a,b) for a in ports for b in ports if a<b)
x=0
while True:
    try:
        print(next(connection))
        x=x+1
    except StopIteration:
        break
print(x)
