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

        E2 = {}
        a = {}
        for i in range(len(examples)):
            if examples[i][attributes[0]] not in a:
                a[examples[i][attributes[0]]] = []
                a[examples[i][attributes[0]]].append(i)
            else:
                a[examples[i][attributes[0]]].append(i)
        # print a
        # print attributes[0]

        E = {}
        P = {}
        for answer in a.iterkeys():
            # print answer
            d = {}
            total = 0
            for key in classes.iterkeys():
                # print key
                u = [value for value in classes[key] if value in a[answer]]
                # print u
                # print len(u)
                d[key] = len(u)
                total += len(u)
            # print d
            # print total

            # Calculate entropy
            # print d
            h = H(d, total)
            # print h
            E[answer] = h

            # Calculate probability for each vote
            p = float(total)/len(examples)
            # print p

            P[answer] = p
            # print "\n"
        # print "ENTROPY:",E
        # print "PROBABILITY:",P

        # Calculate entropy of two attributes
        # H2(E, P)
        h2 = H2(E, P)
        # print "ENTROPY:",h2

        # Compute info gain
        g = hprior - h2
        # print "GAIN:",g

        choose_attrib(examples, attributes)

def H(classes, total):
    '''
    Entropy calculator. Reads number of classes and computes individual entropy
    for each class. Returns the sum of all entropies.
    '''
    e = 0
    log2 = lambda x: math.log(x)/math.log(2)
    for num in classes.itervalues():
        # print num
        val = float(num)/total
        e += -val*log2(val)
    return e

def H2(entropy, probability):
    e = 0
    for key in entropy.iterkeys():
        # print key
        # print entropy[key] * probability[key]
        e += entropy[key] * probability[key]
    # print e
    return e

def choose_attrib(examples, attributes):
    '''
    Returns the best attribute to split on.
    '''
    E = {}          # Single attribute entropies for each classifier
    P = {}          # Probability of classifier
    E2 = {}         # Entropy of two attributes
    att = {}        # Data samples categorized by a given attribute
    c = {}          # Data samples of att{} categorized by Class

    for attribute in attributes:
        print attribute
    # for i in range(len(examples)):
    #     if examples[i][attributes[0]] not in a:
    #         a[examples[i][attributes[0]]] = []
    #         a[examples[i][attributes[0]]].append(i)
    #     else:
    #         a[examples[i][attributes[0]]].append(i)

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
