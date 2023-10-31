ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connection = [(a,b) for a in ports for b in ports]
print(connection)
print(len(connection))

connection = [(a,b)  for a in ports for b in ports if a!=b]
print(connection)
print(len(connection))

connection = [(a,b) for a in ports for b in ports if a<b]
print(connection)
print(len(connection))