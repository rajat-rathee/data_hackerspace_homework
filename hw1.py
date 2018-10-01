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
    return arr
def weigh_pokemons(filename, weight):
    with open(filename) as f:
        data = json.load(f)
    #x = json.dumps(filename)
    index = 0
    names = []
    weightadd = " kg"
    final = str(weight) + weightadd
    for x in data['pokemon']:
        if((data['pokemon'][index]['weight']) == final):
            names.append(data['pokemon'][index]['name'])
        index += 1
    return names

def single_type_candy_count(filename):
    with open(filename) as f:
        data = json.load(f)
    index = 0
    count = 0
    for x in data['pokemon']:
        if(len(data['pokemon'][index]['type']) != 1):
            index += 1
            continue
        else:
            if (data['pokemon'][index]).get('candy_count') == None:
                index += 1
                continue
            else:
                count += (data['pokemon'][index]).get('candy_count')
                index += 1
    print(count)
    return count

def reflections_and_projections(points):
    pass

def normalize(image):
    pass

def sigmoid_normalize(image):
    pass

#histogram_times('airplane_crashes.csv')
#weigh_pokemons('pokedex.json', 10.0)
single_type_candy_count('pokedex.json')