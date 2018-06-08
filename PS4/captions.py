#!/usr/bin/env python2.7
import numpy as np
from ps4 import cosine_sim
import json

with open('dataset.json') as f:
    data = json.load(f)

pixel = np.load('pixel_rep.npy')
vgg = np.load('vgg_rep.npy')
