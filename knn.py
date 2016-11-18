from math import sqrt
from collections import Counter
import matplotlib.pyplot as plt

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
    return (dot_product(v1, v2) / length(v1) * length(v2))

def dot_product(v1, v2):
    s = 0
    for word in v1:
        s += v1[word] * v2[word]
    return s

def length(v):
    s = 0
    for word, score in v.items():
        s += score**2
    return sqrt(s)

def kNN_orig(data, target, k=3):
    if k <= len(data):
        print('K needs to be bigger than number of classes.')
    else:
        distances = []
        for group in data:  # keys
            for features in data[group]:    # values array
                dist = sqrt( (features[0]-target[0])**2 + (features[1]-target[1])**2 )
                distances.append([dist, group])

        votes = [i[1] for i in sorted(distances)[:k]]
        # print(votes)
        # list of tuples, 0th tuple has most common item, 0th index of tuple has group
        print(Counter(votes).most_common(k))

        return Counter(votes).most_common(k)[0][0]

if __name__ == '__main__':
    dataset = {'b': [ [1, 2], [2, 3], [3, 1] ],
            'r': [ [6, 5], [7, 7], [8, 6] ]}
    new_point = [3, 5]

    [ [ plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i] ] for i in dataset ]
    plt.scatter(new_point[0], new_point[1], s=100, marker='*', color=kNN_orig(dataset, new_point))
    plt.show()