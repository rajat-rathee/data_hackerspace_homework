#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import requests
import numpy as np
from collections import defaultdict


def histogram_times(filename):
    arr = [None] * 24
    for l, v in enumerate(arr):
        arr[l] = 0
    time_per = defaultdict(int)
    with open(filename) as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)
    for x in airplane_data[1:]:
        if x[1] == '':
            continue
        else:
            time = (x[1])
        if x[11]:
            num= int(x[11])
            time_per[time] += num
    #time_per[1]
    index = 0
    for x in time_per:
        if(len(x) != 5):
            continue
        else:
            a = x[:2]
            b = x[-2:]
            if(int(b) >= 30):
                c = int(a)
                c += 1
                if c == 24:
                    arr[0] += 1
                else:
                    arr[c] += 1
            else:
                c = int(a)
                if c == 24:
                    arr[0] += 1
                else:
                    arr[c] += 1
    print(arr)
    return arr
def weigh_pokemons(filename, weight):
    with open(filename) as f:
        data = json.load(f)
    #x = json.dumps(filename)
    print(data['pokemon'][0]['weight'])
    weights = []
    names = []
def single_type_candy_count(filename):
    pass

def reflections_and_projections(points):
    pass

def normalize(image):
    pass

def sigmoid_normalize(image):
    pass

histogram_times('airplane_crashes.csv')
#weigh_pokemons('pokedex.json', 10.0)