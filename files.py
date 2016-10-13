import data
import pathlib, pickle, csv

def writeDict(myDict, filename):
    with open('formattedData/' + filename + '.pkl', 'wb') as f:
        pickle.dump(myDict, f)

    with open('formattedData/' + filename + '.csv', 'w', newline = '') as f:
        writer = csv.writer(f)
        for key, value in myDict.items():
           writer.writerow([key, value])

def loadDict(path):
    with path.open(mode = 'rb') as f:
        myDict = pickle.load(f)
    return myDict

def get():
    metadataFilePath = pathlib.Path('formattedData/metadataDict.pkl')
    summariesFilePath = pathlib.Path('formattedData/summariesDict.pkl')
    bagFilePath = pathlib.Path('formattedData/summariesBag.pkl')

    if metadataFilePath.is_file() and summariesFilePath.is_file() and bagFilePath.is_file():
        return loadDict(metadataFilePath), loadDict(bagFilePath)
    else:
        movieMetadata = data.getMovieMetadata()
        movieSummaries, movieSummariesBag = data.getMovieSummaries(movieMetadata)
        movieMetadata = data.fixDict(movieMetadata, movieSummaries)

        writeDict(movieMetadata, 'metadataDict')
        writeDict(movieSummaries, 'summariesDict')
        writeDict(movieSummariesBag, 'summariesBag')

        return movieMetadata, movieSummariesBag

