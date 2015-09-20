#!/usr/bin/env python
#
# This sctipts reads a json file and output a csv file
# Note:  Does not decompose lower level objects
# Brian McKean
#
import fileinput
import json
import csv
import sys

lines = []
for line in fileinput.input():
    lines.append(line)
myjson = json.loads(''.join(lines))
keys = {}
for i in myjson:
    for k in i.keys():
        keys[k] = 1
mycsv = csv.DictWriter(sys.stdout, fieldnames=keys.keys(),
                       quoting=csv.QUOTE_MINIMAL)
mycsv.writeheader()
for row in myjson:
    mycsv.writerow(row)

