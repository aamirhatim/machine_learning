#!/usr/bin/env python2.7
from parse import parse
import ID3
import matplotlib.pyplot as plt

def main():
    e = parse("house_votes_84.data")
    result = []
    split = []

    i = 10
    while i <= 300:
        performance = 0
        for j in range(100):
            training, validation = ID3.split(e, i)              # Split the data
            tree = ID3.ID3(training, ID3.mode(training))        # Run ID3 on training set
            acc = ID3.test(tree, validation)                    # Run validation set on tree
            performance += acc

        result.append(performance/100.0)                        # Add average to array for plotting
        split.append(i)
        i += 10

    plt.plot(split, result)
    plt.show()

if __name__ == "__main__":
    main()
