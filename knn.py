from math import sqrt
from collections import Counter
import matplotlib.pyplot as plt

def kNN(data, target, k=3):
    if k <= len(data):
        print('K needs to be bigger than number of classes.')
    else:
        distances = []
        for group in data:  # keys
            for features in data[group]:    # values array
                dist = sqrt( (features[0]-target[0])**2 + (features[1]-target[1])**2 )
                distances.append([dist, group])

        votes = [i[1] for i in sorted(distances)[:k]]
        # list of tuples, 0th tuple has most common item, 0th index of tuple has group
        print(Counter(votes).most_common(3))

        return Counter(votes).most_common(3)[0][0]

if __name__ == '__main__':
    dataset = {'b': [ [1, 2], [2, 3], [3, 1] ],
            'r': [ [6, 5], [7, 7], [8, 6] ]}
    new_point = [3, 7]

    [ [plt.scatter(ii[0], ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset ]
    plt.scatter(new_point[0], new_point[1], s=100, marker='*', color=kNN(dataset, new_point))
    plt.show()