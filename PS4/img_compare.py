#!/usr/bin/env python2.7
from ps4 import cosine_sim
import json
import numpy as np

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
