#!/usr/bin/env python2.7
import numpy as np

def normalize(matrix):
    squared = matrix**2                         # Square elements
    sums = np.sum(squared)                      # Sum all elements
    norm = np.sqrt(sums)
    return norm

def cosine_sim(a1, a2):
    dot = np.dot(a1.T, a2)                      # Compute dot product of vectors

    mag1 = normalize(a1)                        # Compute magnitutdes of vectors
    mag2 = normalize(a2)

    sim = dot/(mag1*mag2)                       # Calculate similarity
    return sim
