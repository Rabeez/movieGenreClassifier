import files, data, tfidf, knn

# # Import metadata and summaries' bag of words into separate dictionaries
movieData = files.get()
print(len(movieData), 'movies imported')

# # Split data into training/testing sets
train, test = data.split(movieData, 80)
print(len(train), 'training data\n', len(test), 'testing data')

# # Create tfidf vectors for all summaries in the training set
new = {}
count = 0
for key, val in train.items():
    new[key] = val
    count+=1
    if count > 1000: break

movieVectors = files.gettfidf(new)
print(len(new), 'tfidf vectors calculated')

# # Convert a test sample into tfidf
tfidf.tfidf()

# # Apply kNN using cosine similarity
# knn.kNN()

# # Output predicted genre
# print()
