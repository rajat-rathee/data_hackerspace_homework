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
    arr2 = []
    for l, v in enumerate(arr):
        arr[l] = 0
    with open(filename) as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)

    for x in airplane_data[1:]:
        if x[1] == '':
            continue
        else:
            time = (x[1])
            arr2.append(time)
    for x in arr2:
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
    return count

def reflections_and_projections(points):
    pointsarr = np.array(points)
    arrx = []
    arry = []
    final = np.zeros(shape=(2,len(pointsarr[0])))
    for x in pointsarr[0]:
        arrx.append(x)
    for y in pointsarr[1]:
        arry.append(y)
    arrx = np.array(arrx)
    arry = np.array(arry)
    flipy = np.zeros(shape=(len(arry)))
    rotx = np.zeros(shape=(len(arrx)))
    roty = np.zeros(shape=(len(arry)))
    projx = np.zeros(shape=(len(arrx)))
    projy = np.zeros(shape=(len(arry)))
    for y in range(len(arrx)):
        if arry[y] > 1:
            num = 1 - arry[y]
            flipy[y] = 1 - abs(num)
        elif arry[y] == 1:
            flipy[y] = arry[y]
        else:
            num = 1 - arry[y]
            flipy[y] = 1 + abs(num)
    #print(flipy)
    for x in range(len(rotx)):
        rotx[x] = ((arrx[x] * np.cos((np.pi)/2)) - (flipy[x] * np.sin((np.pi)/2)))
        roty[x] = ((flipy[x] * np.cos((np.pi)/2)) + (arrx[x] * np.sin((np.pi)/2)))
    for x in range(len(rotx)):
        projx[x] = (((1/10) * rotx[x]) + ((3/10) * roty[x]))
        projy[x] = (rotx[x]* (3/10)) + (roty[x]*(9/10))

    indexx = 0
    indexy = 0
    for x in final[0]:
        final[0][indexx] = projx[indexx]
        indexx += 1
    for y in final[1]:
        final[1][indexy] = projy[indexy]
        indexy += 1
    return final
def normalize(image):
    arr = np.array(image)
    arr = arr.astype(float)
    max = arr.max()
    min = arr.min()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            num = arr[i][j]
            arr[i][j] = (255/(max-min) * (num - min))
    return arr
def sigmoid_normalize(image, a):
    arr = np.array(image)
    arr = arr.astype(float)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            num = arr[i][j]
            b = 1/-a
            e = np.exp((b*(num - 128)))
            arr[i][j] = 1/(1 + e)
            arr[i][j] *= 255
    arr = arr.astype(int)
    return arr