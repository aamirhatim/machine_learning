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
    if len(examples) == 0:                              # Return default if example set is empty
        return tree(default, default)

    classification = []
    for i in examples:                                  # Otherwise, get classification of all samples
        if i['Class'] not in classification:
            classification.append(i['Class'])

    if len(classification) == 1:                        # Return a tree with label mode(examples) if only one class
        return tree(mode(examples), mode(examples))
    else:                                               # Else, choose the best attribute to split data on
        best = choose_attribute(examples)
        t = tree(best[0], mode(examples))                               # Create tree with label as best attribute
        for branch in best[1].iteritems():
            examplesi = []                              # Reset examplesi for every branch
            for i in branch[1]:
                examplesi.append(examples[i])           # Create new subset of data samples for next iteration of ID3
            subtree = ID3(examplesi, mode(examples))    # Run ID3 algorithm on data subset
            t.children[branch[0]] = subtree             # Add branch to parent Node

    return t

def tree(label, mode):
    '''
    Creates a new tree with a given label.
    '''
    node = Node()                                       # Create instance of Node
    node.label = label                                  # Add label to new node
    node.mode = mode                                    # Add Class mode for the node`
    return node

def mode(examples):
    '''
    Returns most common Class in the set of examples.
    '''
    classes = {}                                        # Create dictionary for classes
    for i in examples:                                  # Search for classes in data set and count their frequency
        if i['Class'] not in classes:
            classes[i['Class']] = 1
        else:
            classes[i['Class']] += 1

    class_mode = 0
    class_label = ''
    for label in classes:                               # Look for class that occurs the most and return its label
        if classes[label] > class_mode:
            class_mode = classes[label]
            class_label = label

    return class_label

def H(classes, total):
    '''
    Entropy calculator. Reads number of classes and computes individual entropy
    for each class. Returns the sum of all entropies.
    '''
    e = 0
    log2 = lambda x: math.log(x)/math.log(2)
    for num in classes.itervalues():
        val = float(num)/total
        if not val == 0:
            e += -val*log2(val)
    return e

def H2(entropy, probability):
    e = 0
    for key in entropy.iterkeys():
        e += entropy[key] * probability[key]
    return e

def choose_attribute(examples):
    '''
    Returns the best attribute to split on.
    '''
    classes = {}    # Dictionary of all Class values
    data = {}       # Dictionary of number of samples in each Class
    E = {}          # Single attribute entropies for each classifier
    P = {}          # Probability of classifier
    E2 = {}         # Entropy of two attributes
    G = {}          # Dictionary of information gain for each attribute
    Gmax = {}       # Attribute with the largest info gain
    att = {}        # Data samples categorized by a given attribute
    branches = {}   # Dictionary of possible branches for each attribute, composed of att{} instances
    c = {}          # Number of data samples of att{} categorized by Class

    # 1. Create dictionary of classes and store sample indexes
    for i in range(len(examples)):
        if examples[i]['Class'] not in classes:
            classes[examples[i]['Class']] = []          # Add new key (Class) if it doesn't already exist
            classes[examples[i]['Class']].append(i)     # Append value to list of sample indexes
        else:
            classes[examples[i]['Class']].append(i)

    # 2. Create dictionary that has number of samples in each Class
    for key in classes.iterkeys():
        data[key] = len(classes[key])
    hprior = H(data, len(examples))                     # Calculate entropy of current distribution (Hprior)

    # 3. Create list of attributes and loop through them all to find the best one
    attributes = examples[0].keys()                     # Create array of attributes using a data sample
    attributes.pop(len(attributes) - 1)                 # Remove last attribute (the Class)

    for attribute in attributes:
        att = {}                                        # Reset att{} for each attribute loop
        E = {}                                          # Reset Entropy dictionary
        P = {}                                          # Reset Probability dictionary

    # 4. Create dictionary of all data samples sorted by classifiers
        for i in range(len(examples)):
            if examples[i][attribute] not in att:       # Add new classifier if it doesn't already exist
                att[examples[i][attribute]] = []
                att[examples[i][attribute]].append(i)
            else:                                       # Else append sample index to classifier key
                att[examples[i][attribute]].append(i)

            branches[attribute] = att                   # Add sorted classifiers to dictionary of branches

    # 5. Sort each att{} key (y/n/?) by Class (democrat/republican)
        for classifier in att.iterkeys():
            c = {}                                      # Reset c{} for each given classifier
            total = 0
            for key in classes.iterkeys():              # Find intersect between classes{} and att{}
                u = [value for value in classes[key] if value in att[classifier]]
                c[key] = len(u)                         # Add size of intersect to dictionary
                total += len(u)                         # Keep track of total number of samples in each Class

            h = H(c, total)                             # Calculate entropy of c{}
            E[classifier] = h                           # Add entropy to dictionary E{} for the given attribute

            p = float(total)/len(examples)              # Calculate probability for each classifier
            P[classifier] = p                           # Add probability to dictionary P{} for given attribute

    # 6. Find information gain for splitting on the given attribute
        h2 = H2(E, P)                                   # Calculate entropy of two attributes = SUM(P * E)
        g = hprior - h2                                 # Compute information gain
        G[attribute] = g                                # Add gain to dictionary G{} for given attribute

    # 7. Find attribute with largest information gain
    max_gain = max(G.values())
    for key in G.iterkeys():
        if G[key] == max_gain:                          # Look for attribute that has matching max_gain value
            return [key, branches[key]]                 # Return split data samples for the best attribute

def split(examples, train_size):
    '''
    Splits data into training and validation sets based on the given parameters.
    '''
    training = []
    validation = []
    sample_set = []

    i = 1
    while i < len(examples) + 1:
        sample_set.append(i)
        i += 1

    j = 0
    while j < train_size:
        r = random.randint(0,len(examples)-1)
        if not sample_set[r] == 0:
            training.append(examples[r])
            sample_set[r] = 0
            j += 1

    for k in sample_set:
        if not k == 0:
            validation.append(examples[k-1])
            sample_set[k-1] = 0

    return (training, validation)

def prune(node, examples):
    '''
    Takes in a trained tree and a validation set of examples. Prunes nodes in order
    to improve accuracy on the validation data; the precise pruning strategy is up to you.
    '''
    results = []
    prune_acc = 0
    pre_prune = test(node, examples)
    print pre_prune

    # Find the best node to prune
    results = prune_tree(node, node, examples, results)
    for i in results:
        if i['accuracy'] > prune_acc:
            prune_acc = i['accuracy']
            best_node = i
    print "BEST"
    print best_node['child'][0]

    # Delete prune_node from the tree if accuracy is better
    if prune_acc > pre_prune:
        print "PRUNING"
        delete_node(node, best_node)

    print test(node, examples)


def prune_tree(node, root, examples, results):
    if len(node.children) == 0:                             # Stop recursion once a leaf node is hit
        return
    else:
        for child in node.children.iteritems():
            # break
            prune_tree(child[1], root, examples, results)            # Keep searching for the bottom of the tree
            # print id(node)
            # print child
            temp = child                                    # Temporarily store the given child in temp
            # print "TEMP:",temp
            # print "START"
            # print node.children
            del node.children[child[0]]                     # Delete the actual child
            # print "DELETED"
            # print node.children
            accuracy = test(root, examples)                  # Run accuracy test on validation set
            results.append({'accuracy':accuracy, 'id':id(node), 'child':temp})
            node.children[temp[0]] = temp[1]                # Restore child and move onto next node
            # print "ADDED"
            # print node.children
            # print child[1].label
            # print "PERCENT:",percent
    return results

def delete_node(node, prune_node):
    # print node.children
    for child in node.children.iteritems():
        if id(node) == prune_node['id']:
            # print child
            # print "ID found"
            if child[0] == prune_node['child'][0]:
                # print "CHILD FOUND"
                del node.children[child[0]]
                print "DELETED"
                # print node.children
                return
        delete_node(child[1], prune_node)




def test(node, examples):
    '''
    Takes in a trained tree and a test set of examples. Returns the accuracy (fraction
    of examples the tree classifies correctly).
    '''
    if len(examples) == 0:                              # Don't test if validation set is empty
        return 0.0

    correct = 0                                         # Initialize counter to keep track of correct classifications
    for i in examples:
        actual = i['Class']                             # Get actual class label
        tested = evaluate(node, i)                      # Get tested class label
        if actual == tested:
            correct += 1                                # Increment correct if sample properly classified
    accuracy = float(correct)/len(examples)             # Calculate accuracy of test
    return accuracy

def evaluate(node, example):
    '''
    Takes in a tree and one example. Returns the Class value that the tree
    assigns to the example.
    '''
    if len(node.children) == 0:                         # If node has no children, then it is a leaf
        label = node.label
    elif not node.children.has_key(example[node.label]):# Return mode of current node if a classifier is not found
        label = node.mode
    else:
        new_node = node.children[example[node.label]]   # Run evaluate() again with new node
        label = evaluate(new_node, example)
    return label
