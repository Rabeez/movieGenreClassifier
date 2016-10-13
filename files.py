import data
import pathlib, pickle, csv

def writeDict(myDict, filename):
    # Save as pickle for later retreival
    with open('formattedData/' + filename + '.pkl', 'wb') as f:
        pickle.dump(myDict, f)

    # Save as csv for viewing
    with open('formattedData/' + filename + '.csv', 'w', newline = '') as f:
        writer = csv.writer(f)
        for key, value in myDict.items():
           writer.writerow([key, value])

def loadDict(path):
    # Load data from pickle
    with path.open(mode = 'rb') as f:
        myDict = pickle.load(f)
    return myDict

def get():
    # Create native path representations for the files
    metadataFilePath = pathlib.Path('formattedData/metadataDict.pkl')
    summariesFilePath = pathlib.Path('formattedData/summariesDict.pkl')
    bagFilePath = pathlib.Path('formattedData/summariesBag.pkl')

    # Load data from files if they exist
    if metadataFilePath.is_file() and summariesFilePath.is_file() and bagFilePath.is_file():
        return loadDict(metadataFilePath), loadDict(bagFilePath)
    else:
        # Otherwise import data from the corpus
        movieMetadata = data.getMovieMetadata()
        movieSummaries, movieSummariesBag = data.getMovieSummaries(movieMetadata)
        movieMetadata = data.fixDict(movieMetadata, movieSummaries)

        # And write it to the files
        writeDict(movieMetadata, 'metadataDict')
        writeDict(movieSummaries, 'summariesDict')
        writeDict(movieSummariesBag, 'summariesBag')

        return movieMetadata, movieSummariesBag

