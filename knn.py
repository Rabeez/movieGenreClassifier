import numpy, collections

def knn(data, target, k = 3):
    if k >= len(data):
        print('K needs to be smaller than number of data points.')
    else:
        distances = []
        for group in data:
            for features in data[group]:
                dist = numpy.linalg.norm(numpy.array(features), numpy.array(target))
                distances.append([dist, group])

        votes = [i[1] for i in sorted(distances)[:k]]
        print(collections.Counter(votes).most_common(3))

        return collections.Counter(votes).most_common(3)