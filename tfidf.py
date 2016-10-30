import math

def tfidf(data):
    # Calculate tfidf vectors for all movies
    tfidfVector = {}
    idfVector = idf(data)
    print(len(idfVector), ' unique words')

    i = 1
    for movieID, movieData in data.items():
        tfVector = extend(normalize(movieData[2]), data)  # summary bag
        tfidfVector[movieID] = mult(tfVector, idfVector)
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
    out = {}
    for movieID, movieData in data.items():
        for word, freq in movieData[2].items():
            if word in out:
                out[word] += 1
            else:
                out[word] = 1
    return {word: 1+math.log(len(data)/freq) for word, freq in out.items()}

def mult(tfVector, idfVector):
    # Return vector with products of corresponding entries in tf and idf vectors
    return {word: freq*idfVector[word] for word, freq in tfVector.items()}

