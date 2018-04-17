from node import Node
import math
import random
import numpy as np

def ID3(examples, default):
    '''
    Takes in an array of examples, and returns a tree (an instance of Node)
    trained on the examples.  Each example is a dictionary of attribute:value pairs,
    and the target class variable is a special attribute with the name "Class".
    Any missing attributes are denoted with a value of "?"
    '''
    # Return default if example set is empty
    if len(examples) == 0:
        return default
    # Else choose the best attribute
    else:
    # 1. Find best attribute to split on
        classes = {}                                    # Create dictionary of classes and store sample indexes
        for i in range(len(examples)):
            if examples[i]['Class'] not in classes:
                classes[examples[i]['Class']] = []      # Add new key (Class) if it doesn't already exist
                classes[examples[i]['Class']].append(i) # Append value to list of sample indexes
            else:
                classes[examples[i]['Class']].append(i)

        data = {}                                       # Create dictionary that has number of samples in each Class
        for key in classes.iterkeys():
            data[key] = len(classes[key])
        hprior = H(data, len(examples))                 # Calculate entropy of current distribution (Hprior)

        attributes = examples[0].keys()                 # Create array of attributes using a data sample
        attributes.pop(len(attributes) - 1)             # Remove last attribute (the Class)

        best = choose_attrib(examples, attributes, classes, hprior)

    # 2. Create new tree with root at best attribute
        n = Node()                                      # Initialize node
        n.label = best[0]                               # Set node label to best attribute
        for branch in best[1]:
            print branch

def H(classes, total):
    '''
    Entropy calculator. Reads number of classes and computes individual entropy
    for each class. Returns the sum of all entropies.
    '''
    e = 0
    log2 = lambda x: math.log(x)/math.log(2)
    for num in classes.itervalues():
        val = float(num)/total
        e += -val*log2(val)
    return e

def H2(entropy, probability):
    e = 0
    for key in entropy.iterkeys():
        e += entropy[key] * probability[key]
    return e

def choose_attrib(examples, attributes, classes, hprior):
    '''
    Returns the best attribute to split on.
    '''
    E = {}          # Single attribute entropies for each classifier
    P = {}          # Probability of classifier
    E2 = {}         # Entropy of two attributes
    G = {}          # Dictionary of information gain for each attribute
    Gmax = {}       # Attribute with the largest info gain
    att = {}        # Data samples categorized by a given attribute
    branches = {}   # Dictionary of possible branches for each attribute, composed of att{} instances
    c = {}          # Data samples of att{} categorized by Class

    for attribute in attributes:
        att = {}                                        # Reset att{} for each attribute loop

    # 1. Create dictionary of all data samples sorted by classifiers
        for i in range(len(examples)):
            if examples[i][attribute] not in att:       # Add new classifier if it doesn't already exist
                att[examples[i][attribute]] = []
                att[examples[i][attribute]].append(i)
            else:                                       # Else append sample index to classifier key
                att[examples[i][attribute]].append(i)

            branches[attribute] = att                   # Add sorted classifiers to dictionary of branches

    # 2. Sort each att{} key (y/n/?) by Class (democrat/republican)
        for classifier in att.iterkeys():
            c = {}                                      # Reset c{} for each given classifier
            total = 0
            for key in classes.iterkeys():              # Find intersect between classes{} and att{}
                u = [value for value in classes[key] if value in att[classifier]]
                c[key] = len(u)                         # Add size of intersect to dictionary
                total += len(u)                         # Keep track of total number of samples in ea h Class

            h = H(c, total)                             # Calculate entropy of c{}
            E[classifier] = h                           # Add entropy to dictionary E{} for the given attribute

            p = float(total)/len(examples)              # Calculate probability for each classifier
            P[classifier] = p                           # Add probability to dictionary P{} for given attribute

    # 3. Find information gain for splitting on the given attribute
        h2 = H2(E, P)                                   # Calculate entropy of two attributes = SUM(P * E)
        g = hprior - h2                                 # Compute information gain
        G[attribute] = g                                # Add gain to dictionary G{} for given attribute

    # 4. Find attribute with largest gain value
    max_gain = max(G.values())
    for key in G.iterkeys():
        if G[key] == max_gain:                          # Look for attribute that has matching max_gain value
            return [key, branches[key]]                 # Return split data samples for the best attribute

def prune(node, examples):
    '''
    Takes in a trained tree and a validation set of examples.  Prunes nodes in order
    to improve accuracy on the validation data; the precise pruning strategy is up to you.
    '''

def test(node, examples):
    '''
    Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
    of examples the tree classifies correctly).
    '''


def evaluate(node, example):
    '''
    Takes in a tree and one example.  Returns the Class value that the tree
    assigns to the example.
    '''
