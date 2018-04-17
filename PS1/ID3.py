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
        # Create dictionary of classes and count how many times they show up
        # classes = get_classifiers(examples, 'Class')
        classes = {}
        for i in range(len(examples)):
            if examples[i]['Class'] not in classes:
                classes[examples[i]['Class']] = []
                classes[examples[i]['Class']].append(i)
            else:
                classes[examples[i]['Class']].append(i)
        data = {}
        for key in classes.iterkeys():
            data[key] = len(classes[key])
        # print data
        # print classes['republican']

        # Initialize Node
        n = Node()

        # Calculate entropy of current distribution (Hprior)
        # H(classes, len(examples))
        hprior = H(data, len(examples))
        # print "HPRIOR:",hprior

        # Get list of attributes and choose the best one to split on
        attributes = examples[0].keys()
        attributes.pop(len(attributes) - 1)         # Remove last attribute (the Class)

        choose_attrib(examples, attributes, classes, hprior)

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

    # 2. Sort each att{} key (y/n/?) by Class (democrat/republican)
        for classifier in att.iterkeys():
            c = {}                                      # Reset c{} for each given classifier
            total = 0
            for key in classes.iterkeys():              # Find intersect between classes{} and att{}
                u = [value for value in classes[key] if value in att[classifier]]
                c[key] = len(u)                         # Add size of intersect to dictionary
                total += len(u)                         # Keep track of total number of samples

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
            Gmax[key] = max_gain                        # Add key/value pair to single element dictionary Gmax{}
            break
    print Gmax

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
