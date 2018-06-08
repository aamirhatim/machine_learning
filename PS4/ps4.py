#!/usr/bin/env python2.7
import numpy as np
import json
import sys

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

def find_neighbor(test_name, train, images, captions, pixel, vgg):
    # test_name = test[0]                                   # Start by finding similarity to first image in training set
    test_ind = images.index(test_name)                      # Get index of test image in the images set
    train_ind = images.index(train[0])                      # Get index of training image in the images set

    pixel_train = pixel[train_ind]                          # Get pixel representation of training image
    pixel_test = pixel[test_ind]                            # Get pixel representation of test image
    sim = cosine_sim(pixel_test, pixel_train)               # Compute baseline similarity for pixel rep
    best_pixel = {'name':train[0], 'similarity':sim}        # Initialize best pixel value for comparison with rest of the training set

    vgg_train = vgg[train_ind]                              # Get vgg representation of training image
    vgg_test = vgg[test_ind]                                # Get vgg representation of test image
    sim = cosine_sim(vgg_test, vgg_train)                   # Compute baseline similarity for vgg rep
    best_vgg = {'name':train[0], 'similarity':sim}          # Initialize best vgg value for comparison with rest of the training set

    for i in range(len(train)-1):                           # Cycle through remainder of training set
        train_ind = images.index(train[i+1])                # Get index

        pixel_train = pixel[train_ind]                      # Get pixel representations
        pixel_test = pixel[test_ind]
        sim = cosine_sim(pixel_test, pixel_train)           # Compute similarity for pixel rep
        if sim > best_pixel['similarity']:                  # Check if similarity is better than current 'best' value
            best_pixel['name'] = train[i+1]
            best_pixel['similarity'] = sim

        vgg_train = vgg[train_ind]                          # Get vgg representations
        vgg_test = vgg[test_ind]
        sim = cosine_sim(vgg_test, vgg_train)               # Compute similarity for vgg rep
        if sim > best_vgg['similarity']:                    # Check if similarity is better than current 'best' value
            best_vgg['name'] = train[i+1]
            best_vgg['similarity'] = sim

    return best_pixel, best_vgg

def captions():
    with open('dataset.json') as f:
        data = json.load(f)
    train = data['train']                                   # File names of training images
    test = data['test']                                     # File names of test images
    images = data['images']                                 # File names of all images
    captions = data['captions']                             # Captions for each image

    pixel = np.load('pixel_rep.npy')                        # Load pixel and vgg representations of images
    vgg = np.load('vgg_rep.npy')

    txt_pixel = open('pixel.txt','w')                       # Open txt files for export
    txt_vgg = open('vgg.txt','w')

    for i in test:
        # Find nearest neighbor uing cosine similarity
        neighbor_pixel, neighbor_vgg = find_neighbor(i, train, images, captions, pixel, vgg)

        # Find caption of neighbor and write it to txt file
        print >>txt_pixel, captions[neighbor_pixel['name']]
        print >>txt_vgg, captions[neighbor_vgg['name']]

    txt_pixel.close()                                       # Close files
    txt_vgg.close()
