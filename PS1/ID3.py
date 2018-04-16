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

        # print classes['republican']


        # Initialize Node
        n = Node()

        # Calculate entropy of current distribution (Hprior)
        # n.h = H(classes, len(examples))

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
        print attributes[0]

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
            h = H(d, total)
            # print h
            E[answer] = h

            # Calculate probability for each vote
            p = float(total)/len(examples)
            # print p

            P[answer] = p
            # print "\n"
        print E
        print P

        # Calculate entropy of two attributes
        H2(E, P)
        # h2 = H2(E, P)
        # print h2

        # u = [value for value in classes['republican'] if value in a['y']]
        # u2 = [value for value in classes['democrat'] if value in a['y']]


        # choose_attrib(examples, attributes)
        # a = {}
        # for i in classes['democrat']:
        #     if examples[i][attributes[0]] not in a:
        #         a[examples[i][attributes[0]]] = []
        #         a[examples[i][attributes[0]]].append(i)
        #     else:
        #         a[examples[i][attributes[0]]].append(i)
        # print a,"\n"
##################################################################3
        # for j in attributes:
        #     print j
        #     split = {}
        #     for key, val in classes.iteritems():
        #         a = {}
        #         for i in val:
        #             if examples[i][j] not in a:
        #                 a[examples[i][j]] = 1
        #                 # a[examples[i][attributes[0]]].append(i)
        #             else:
        #                 a[examples[i][j]] += 1
        #                 # a[examples[i][attributes[0]]].append(i)
        #             # print i
        #         split[key] = a
        #         # print c
        #
        #     for i in split.itervalues():
        #         for j in i.iterkeys():
        #             print j
        #         print i
        #
        #
        #     print "\n"

def get_classifiers(examples, class_name):
    classifiers = {}
    i = 0
    for key in iter(examples):
        # print examples.index(key)
        if key[class_name] not in classifiers:
            classifiers[key[class_name]] = 1
        else:
            classifiers[key[class_name]] += 1
    return classifiers

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
        print key
        print entropy[key] * probability[key]

def choose_attrib(examples, attributes):
    '''
    Returns the best attribute to split on.
    '''
    gain = 0                                            # Initialize info gain
    # Calculate entropy for each split and the info gain
    for a in attributes:
        classifiers = get_classifiers(examples, a)      # Determine classifiers in sample set

        h = H(classifiers, len(examples))               # Calculate entropy

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
