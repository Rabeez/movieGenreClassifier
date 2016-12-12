import math
# from collections import Counter
# import matplotlib.pyplot as plt

def kNN(data, target, k=10):
    if k >= len(data):
        print('K needs to be bigger than number of data points.')
    else:
        distances = []
        for movieID, vector in data.items():  # keys
            dist = cosine_similarity(vector, target)
            distances.append([dist, movieID])

        k_nearest = [i[1] for i in sorted(distances)[:k]]
        return k_nearest

def cosine_similarity(v1, v2):
    return (dot_product(v1, v2) / (length(v1) * length(v2)))

def dot_product(v1, v2):
    s = 0
    for word in v1:
        s += v1[word] * v2[word]
    return s

def length(v):
    s = 0
    for word, score in v.items():
        s += score**2
    return math.sqrt(s)
