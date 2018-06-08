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

def img_compare():
    with open('cnn_dataset.json') as f:                 # Load dataset
        data = json.load(f)

    mj1_pixel = np.array(data['pixel_rep']['mj1'])      # Separate image data for pixel_rep
    mj2_pixel = np.array(data['pixel_rep']['mj2'])
    cat_pixel = np.array(data['pixel_rep']['cat'])

    mj1_vgg = np.array(data['vgg_rep']['mj1'])          # Separate image data for vgg_rep
    mj2_vgg = np.array(data['vgg_rep']['mj2'])
    cat_vgg = np.array(data['vgg_rep']['cat'])

    print 'PIXEL'
    print 'mj1-mj2:',cosine_sim(mj1_pixel, mj2_pixel)
    print 'mj1-cat:',cosine_sim(mj1_pixel, cat_pixel)
    print 'mj2-cat:',cosine_sim(mj2_pixel, cat_pixel)

    print '\nVGG'
    print 'mj1-mj2:',cosine_sim(mj1_vgg, mj2_vgg)
    print 'mj1-cat:',cosine_sim(mj1_vgg, cat_vgg)
    print 'mj2-cat:',cosine_sim(mj2_vgg, cat_vgg)

def captions():
    with open('dataset.json') as f:
        data = json.load(f)

    pixel = np.load('pixel_rep.npy')
    vgg = np.load('vgg_rep.npy')
