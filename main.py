import files, knn

# Import metadata and summaries' bag of words into separate dictionaries
movieMetadata, movieSummaries = files.get()
print(len(movieMetadata), 'movies imported')

# d = {1: [10, 11, 12], 2: [20, 22, 25], 5: [52, 57, 59]}

# print(knn.knn(d, [5, 7, 9], 2))