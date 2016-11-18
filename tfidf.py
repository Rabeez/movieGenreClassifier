import math

def tfidf(data):
    # Calculate tfidf vectors for all movies
    tfidfVector = {}
    idfVector = idf(data)
    print(len(idfVector), ' unique words')

    i = 1
    for movieID, movieData in data.items():
        tfVector = extend(movieData[2], data)  # summary bag
        tfidfVector[movieID] = normalize(mult(tfVector, idfVector))
        print(i, ' movie(s) done')
        i+=1
    return tfidfVector

def extend(bag, data):
    # Add empty entries for words to extend dimension of bag vector
    out = bag.copy()
    for movieID, movieData in data.items():
        for word, freq in movieData[2].items():
            if not word in bag:
                out[word] = 0
    return out

def normalize(bag):
    # Return unit vector of bag
    return {key: val/len(bag) for key, val in bag.items()}

def idf(data):
    # Calculate idf vector for the dataset
    allWordsdf = {}
    for movieID, movieData in data.items():
        for word, freq in movieData[2].items():
            if not word in allWordsdf:
                allWordsdf[word] = 0

    for word, freq in allWordsdf.items():
        for movieID, movieData in data.items():
            if word in movieData[2]:
                allWordsdf[word] += 1
                continue

    return {word: math.log(len(data)/freq) for word, freq in allWordsdf.items()}

def mult(tfVector, idfVector):
    # Return vector with products of corresponding entries in tf and idf vectors
    return {word: freq*idfVector[word] for word, freq in tfVector.items()}

