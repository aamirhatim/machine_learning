#!/usr/bin/env python2.7
import pandas as pd
from random import randint

num_att = 10
num_samples = 20

data = []
for i in range(num_samples):
    empty = []
    data.append(empty)

for i in range(num_samples):                # Populate all but last attribute with binary values
    for j in range(num_att-1):
        data[i].append(randint(0,1))

count = 0
while count < num_samples/2:                # Classify half of data as 1 and the other half as 0
    data[count].append(1)
    count += 1
while count < num_samples:
    data[count].append(0)
    count += 1

for i in data:
    print i
