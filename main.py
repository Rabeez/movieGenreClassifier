import files, data, tfidf, knn

# # Import metadata and summaries' bag of words into separate dictionaries
movieData = files.get()
print(len(movieData), 'movies imported')

# # Split data into training/testing sets
train, test = data.split(movieData, 80)
print(len(train), 'training data')
print(len(test), 'testing data')

for key, value in test.items():
    value[-1] = True

# # Create tfidf vectors for all summaries
newTrain = {}
count = 0
for key, val in train.items():
    newTrain[key] = val
    count += 1
    if count >= 1000: break

newTest = {}
count = 0
for key, val in test.items():
    newTest[key] = val
    count += 1
    if count >= 5: break

# newTrain = {
#     1: ['movie1', ['genre1'], {'the':1, 'game': 2, 'of':2, 'life':1, 'is':1, 'a':1, 'everlasting':1, 'learning': 1}, False]
#     # ,2: ['movie2', ['genre2'], {'the': 1, 'unexamined':1, 'life':1, 'is':1, 'not':1, 'worth':1, 'living':1}, False]
# }
# newTest = {
#     # 3: ['movie3', ['genre3'], {'never':1, 'stop': 1, 'learning':1}, True].
#     4: ['movie4', ['genre4'], {'life':1, 'learning': 1}, True]
# }
# print(newTest)

trainVectors, testVectors = tfidf.tfidf(newTrain, newTest)
print(len(trainVectors) + len(testVectors), 'tfidf vectors calculated')
# print(trainVectors)
# print(testVectors)

# # Apply kNN using cosine similarity
genres = {}
for key in testVectors:
    k_nearest = knn.kNN(trainVectors, testVectors[key], 50)
    genres[key] = {}
    for movieID in k_nearest:
        temp_genres = movieData[movieID][1]
        for genre in temp_genres:
            if genre in genres[key]:
                genres[key][genre] += 1
            else:
                genres[key][genre] = 1

# # Output predicted genre
print('\nPredictions')
top = 10
# print(genres)
for movieID, genreCounts in genres.items():
    print(movieID, ':')
    for _ in range(top):
        if genreCounts:
            print(max(genreCounts, key=genreCounts.get), genreCounts[max(genreCounts, key=genreCounts.get)])
            genreCounts.pop(max(genreCounts, key=genreCounts.get))
        else:
            print('Empty')
    print()
