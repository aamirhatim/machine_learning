#!/usr/bin/env python2.7
from parse import parse
import ID3
import matplotlib.pyplot as plt

def main():
    e = parse("house_votes_84.data")
    result = []
    prune_result = []
    split = []

    i = 10
    while i <= 300:
        performance = 0
        prune_performance = 0
        for j in range(100):
            training, validation = ID3.split(e, i)              # Split the data
            tree = ID3.ID3(training, ID3.mode(training))        # Run ID3 on training set
            acc = ID3.test(tree, validation)                    # Run validation set on tree
            performance += acc

            ID3.prune(tree, validation)                             # Prune the tree
            acc = ID3.test(tree, validation)                    # Run validation set on pruned tree
            prune_performance += acc

        result.append(performance/100.0)                        # Add average to array for plotting
        prune_result.append(prune_performance/100.0)
        split.append(i)
        i += 100

    plt.plot(split, prune_result)
    plt.hold(True)
    plt.plot(split, result)
    plt.show()

if __name__ == "__main__":
    main()
