#!/usr/bin/env python2.7
import csv
from random import randint

num_att = 200                               # number of attributes
num_samples = 1000                          # Number of samples

data = []                                   # Create empty dataset

data.append([])                             # Add header row
for i in range(num_att):
    att_name = 'att_'+str(i)
    data[0].append(att_name)
data[0].append('class')

for i in range(num_samples):                # Add empty list for each sample
    empty = []
    data.append(empty)

for i in range(num_samples):                # Populate all but last attribute with binary values
    for j in range(num_att-1):
        data[i+1].append(randint(0,1))

count = 0
while count < (num_samples)/2:
    data[count+1].append(1)                 # Make last attribute a 1 for half of data
    data[count+1].append('True')            # Set class as True for half the data
    count += 1
while count < num_samples:
    data[count+1].append(0)                 # Make last attribute a 0 for second half of data
    data[count+1].append('False')           # Set class as False for second half of data
    count += 1

with open('q1.csv', 'w') as output:         # Export as CSV
    csvWriter = csv.writer(output, delimiter = ',')
    csvWriter.writerows(data)
