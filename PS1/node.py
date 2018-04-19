class Node:
    def __init__(self):
        self.label = None                   # Name of attribute the node is split on
        self.children = {}                  # Dictionary of child branches and the data sets inside them
        self.mode = None                    # Mode class of all samples in node
