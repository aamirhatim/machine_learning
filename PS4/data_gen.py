#!/usr/bin/env python2.7
import csv
from random import randint
import numpy as np

def init_dataset(num_att, num_samples):
    data = []                                   # Create empty dataset

    data.append([])                             # Add header row
    for i in range(num_att):
        att_name = 'att_'+str(i)
        data[0].append(att_name)
    data[0].append('class')

    for i in range(num_samples):                # Add empty list for each sample
        empty = []
        data.append(empty)

    return data

def generate_dt_nn(data, num_att, num_samples):
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

def generate_nb_mlp(data, num_att, num_samples):
    classes = []
    for i in range(num_att):
        classes.append('class_'+str(i))

    for i in range(num_samples):
        for j in range(num_att):
            dist = np.random.normal(1+(j*(-1**j)/num_att),10)
            data[i+1].append(dist)
        c = data[i+1].index(max(data[i+1]))
        data[i+1].append(classes[c])

    with open('q3.csv', 'w') as output:         # Export as CSV
        csvWriter = csv.writer(output, delimiter = ',')
        csvWriter.writerows(data)

samples = 1000
## PROBLEM 1 ##
# attributes = 200
# dataset = init_dataset(attributes, samples)     # Init dataset for DT/NN performance
# generate_dt_nn(dataset, attributes, samples)    # Populate data

## PROBLEM 2 ##
# attributes = 20
# dataset = init_dataset(attributes, samples)     # Init dataset for Naive Bayes/MLP performance
# generate_nb_mlp(dataset, attributes, samples)   # Populate data
