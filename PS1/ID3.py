from node import Node
import math

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
    else:
        return 1

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

def H(pos, neg, s):
    '''
    Entropy calculator. Takes in number of positive samples (pos), number of negative
    samples (neg), and total number of samples (s). Returns entropy of sample set.
    '''
    p = float(pos/s)
    n = float(neg/s)
    h = -p*math.log(p) - n*math.log(n)
    return h
