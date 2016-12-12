import unicodedata, re, math, nltk

def getMovieMetadata():
    # Open file in read mode with unicode encoding
    metadataFile = open('rawData/movie.metadata.tsv', 'r', encoding='utf8').readlines()

    movieMetadata = {}
    # candidates = {'Action': 0, 'Adventure': 0, 'Comedy': 0, 'Crime Fiction': 0, 'Documentary': 0, 'Drama': 0, 'Family Film': 0, 'Romance Film': 0, 'Thriller': 0, 'Short Film': 0}
    for movie in metadataFile:  # Loop over all lines (movies) in file
        # Extract basic information for storage
        movieID = movie.split('\t')[0]
        movieTitle = movie.split('\t')[2]

        # Extract language for filter
        movieLangDict = eval(movie.split('\t')[6])
        movieLangs = [langName for langID, langName in movieLangDict.items()]

        # Extract country of origin for filter
        movieOriginDict = eval(movie.split('\t')[7])
        movieOrigins = [originName for originID, originName in movieOriginDict.items()]
        # Extract genre for storage
        movieGenresDict = eval(movie.split('\t')[8])
        movieGenres = [genreName for genreID, genreName in movieGenresDict.items()]

        # Evaluate filters
        if len(movieGenres) < 1: continue
        if not len(movieLangs) == 1: continue
        if not 'United States of America' in movieOrigins: continue
        if not 'English Language' in movieLangs: continue
        inValidGenre = False 
        candidates = ['Thriller', 'Drama', 'Comedy']
        for genre in movieGenres:
            if not genre in candidates:
                inValidGenre = True
                break
        if inValidGenre: continue

        # Save useful metadata after changing encoding of title
        movieTitle = unicodedata.normalize('NFKD', movieTitle).encode('ascii','ignore').decode('ascii')
        movieMetadata[movieID] = [movieTitle, movieGenres]

    return movieMetadata

def getMovieSummaries(movieMetadata):
    # Open file in read mode with unicode encoding
    summariesFile = open('rawData/plot_summaries.txt', 'r', encoding='utf8').readlines()

    movieSummaries = {}
    movieSummariesBag = {}
    genreCounts = {}
    for movie in summariesFile:  # Loop over all lines (summaries) in file
        # Extract information for storage
        movieID = movie.split('\t')[0]
        movieSummary = movie.split('\t')[1]

        # Evaluate filters
        if not movieID in movieMetadata: continue
        stopCharFound = False
        for stopChar in ['{', '}', '<', '>', '[', ']', '(', ')', '&', '/']:
            if stopChar in movieSummary:
                stopCharFound = True
                break
        if stopCharFound: continue
        if len(movieSummary) < 500: continue

        # Genre counter
        movieGenres = [genreName for genreName in movieMetadata[movieID][1]]
        for genre in movieGenres:
            if genre in genreCounts:
                genreCounts[genre] += 1
            else:
                genreCounts[genre] = 1

        # Genre cap
        skipping = False
        for genre in movieGenres:
            if genreCounts[genre] > 100:
                skipping = True
                break
        if skipping: continue

        movieSummary = re.sub('%', ' percent ', movieSummary)
        movieSummary = re.sub('[^a-zA-Z\d\s:;?.,"\'$!#+`\-]', ' ', movieSummary)
        movieSummary = unicodedata.normalize('NFKD', movieSummary).encode('ascii','ignore').decode('ascii')

        # Save summary and its bag of words representation
        movieSummaries[movieID] = movieSummary
        movieSummariesBag[movieID] = bagOfWords(movieSummary)

    print(genreCounts)
    return movieSummaries, movieSummariesBag

def fixDict(movieMetadata, movieSummaries):
    # Only keep the movies in movieMetadata which are also in movieSummaries
    return {movieID: movieData for movieID, movieData in movieMetadata.items() if movieID in movieSummaries}

def bagOfWords(text):
    # Apply preprocessing
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()

    # Tokenize the text into words
    tknzr = nltk.tokenize.RegexpTokenizer(r'\w+')
    words = tknzr.tokenize(text)

    # Remove all stop words
    stopWords = set(nltk.corpus.stopwords.words('english'))
    words = [w for w in words if w not in stopWords]

    # Stem all words
    stemr = nltk.stem.PorterStemmer()
    words = [stemr.stem(w) for w in words]

    # Populate frequency dictionary 
    freqDict = {}
    for word in words:
        if word not in freqDict:
            freqDict[word] = 1
        else:
            freqDict[word] += 1

    return freqDict

def combineDict(dict1, dict2):
    # Combine dict1 and dict2
    # --> Assumes both have all the same keys and dict1 has list values
    output = {}
    for key, valList in dict1.items():
        newValList = valList.copy()
        newValList += [dict2[key], False]   # Bool is a placeholder
        output[key] = newValList
    return output

def split(data, percentage):
    # Create 2 dicts of appropriate size
    splitPoint = math.floor(len(data) * (percentage/100))
    return dict(list(data.items())[:splitPoint]), dict(list(data.items())[splitPoint:])

