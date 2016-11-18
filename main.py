import files, data, tfidf, knn

# # Import metadata and summaries' bag of words into separate dictionaries
movieData = files.get()
print(len(movieData), 'movies imported')

# # Split data into training/testing sets
train, test = data.split(movieData, 80)
print(len(train), 'training data\n', len(test), 'testing data')

for key, value in test.items():
    value[-1] = True

# # Create tfidf vectors for all summaries
newTrain = {}
count = 0
for key, val in train.items():
    newTrain[key] = val
    count += 1
    if count >= 100: break

newTest = {}
count = 0
for key, val in test.items():
    newTest[key] = val
    count += 1
    if count >= 1: break

trainVectors, testVectors = tfidf.tfidf(newTrain, newTest)
print(len(trainVectors) + len(testVectors), 'tfidf vectors calculated')

# # Apply kNN using cosine similarity
genres = {}
for key in testVectors:
    k_nearest = knn.kNN(trainVectors, testVectors[key])
    genres[key] = {}
    for movieID in k_nearest:
        temp_genres = movieData[movieID][1]
        for genre in temp_genres:
            if genre in genres[key]:
                genres[key][genre] += 1
            else:
                genres[key][genre] = 1

# final_genres = {}
# for movieID, genreCounts in genres.items():
#     for genre, count in genreCounts.items():
#         if count > 1

# # Output predicted genre
print(genres)
