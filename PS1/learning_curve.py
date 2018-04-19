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
        print "Plotting:",i,"training size"
        performance = 0
        prune_performance = 0
        for j in range(100):
            training, validation = ID3.split(e, i)              # Split the data
            tree = ID3.ID3(training, ID3.mode(training))        # Run ID3 on training set
            acc = ID3.test(tree, validation)                    # Run validation set on tree
            performance += acc

            ID3.prune(tree, validation)                         # Prune the tree
            acc = ID3.test(tree, validation)                    # Run validation set on pruned tree
            prune_performance += acc

        result.append(performance)                              # Add average to array for plotting
        prune_result.append(prune_performance)
        split.append(i)
        i += 10

    # Plot the results
    plt.title("Pruned vs. Un-Pruned Decision Tree")
    plt.plot(split, prune_result, marker = 'o', linestyle = '-', label = 'Pruned', color = 'purple')
    plt.hold(True)
    plt.plot(split, result, marker = 'o', linestyle = '-', label = 'Un-pruned', color = 'black')
    plt.xlabel("Size of Training Data")
    plt.ylabel("Accuracy (%)")
    plt.xlim(0,300)
    plt.ylim(80,100)
    plt.grid(True)
    plt.legend(loc = 'upper right')
    plt.show()

if __name__ == "__main__":
    main()
