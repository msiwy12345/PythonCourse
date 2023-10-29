import urllib.request
import os


data_dir = r"/home/siwy/python/section1"

pages = [
    {"name": "mobilo", "url": "http://www.mobilo24.eu/"},
    {"name": "nonexistent", "url": "http://abc.cde.fgh.ijk.pl/"},
    {"name": "kursy", "url": "http://www.kursyonline24.eu/"},
]

for i in pages:
    try:
        file_name="{}.html".format(i["name"])
        path = os.path.join(data_dir, file_name)

        print("processing {} --> {}".format(i["url"], file_name))
        urllib.request.urlretrieve(i["url"], path)
        print('done')
    except:
        print('failure')
        break

else:
    print('download succesful')