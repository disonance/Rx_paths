import csv
import re
import numpy as np
import matplotlib.pyplot as plt

#filename = raw_input("Input File - > ")
filename = '/Users/dennisngsze_yang/Documents/WiPASX_0_0/test_station_output_wipas/Cellular Station 2_JP_2017-08-25_18-36-27.csv'
search_str = raw_input("Search Str ->")
f1 = open(filename, "rU")
f2 = open("new.txt","w+")
f1.readline()

path = []
data = []
reader = csv.DictReader(f1)

header = reader.fieldnames

for line in header:
    f2.write(line + '\r\n' )
    mdata = re.search(search_str,line)

    if mdata:
        # print line
        path.append(line)

for row in reader:
    if row['SerialNumber'] == '':
        continue
    for key in path:
        print key + ' = ' + row[key]
        data.append(row[key])

plt.plot(data)
plt.show()