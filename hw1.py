#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    a = [None] * 24
    for l, v in enumerate(a):
        a[l] = 0
    data = np.loadtxt(filename, delimiter= ',', skiprows=1)
    data1 = data[:,1]
    for c in data1:
        print(c)
def weigh_pokemons(filename, weight):
    pass

def single_type_candy_count(filename):
    pass

def reflections_and_projections(points):
    pass

def normalize(image):
    pass

def sigmoid_normalize(image):
    pass

histogram_times('airplane_crashes.csv')