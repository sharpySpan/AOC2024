import os
import re

readfile = open('list.txt', 'r')

split = re.split(r'\n', readfile.read())


for line in range(len(split)):
    split[line] = int(split[line])


print(split)