from node import Node
import math
import random

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
        classes = get_classifiers(examples, 'Class')

        # Initialize Node
        n = Node()

        # Calculate entropy of current distribution (Hprior)
        total = len(examples)
        n.h = H(classes, total)

        # Get list of attributes and choose the best one to split on
        attributes = examples[0].keys()
        attributes.pop(len(attributes) - 1)         # Remove last attribute (the Class)
        choose_attrib(examples, attributes)

def get_classifiers(examples, class_name):
    classifiers = {}
    for key in iter(examples):
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

def choose_attrib(examples, attributes):
    '''
    Returns the best attribute to split on.
    '''
    # Calculate entropy for each split and the info gain
    for a in attributes:
        classifiers = get_classifiers(examples, a)
        print classifiers

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
