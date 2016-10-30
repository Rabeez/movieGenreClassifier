import files, data, knn

# Import metadata and summaries' bag of words into separate dictionaries
movieData = files.get()
print(len(movieData), 'movies imported')

# Split data into training/testing sets
train, test = data.split(movieData, 80)
print(len(train), 'training data\n', len(test), 'testing data')

# # Create tfidf vectors for all summaries in the training set
movieVectors = tfidf(train)

# # Convert a test sample into tfidf
# tfidf()

# # Apply kNN using cosine similarity
# kNN()

# # Output predicted genre
# print()
