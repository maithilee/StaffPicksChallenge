import os, sys, csv
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.models.doc2vec import TaggedDocument, Doc2Vec

PROJECT_DIR = os.getcwd()

# Make a dictionary which gives the category numbers to which each clip_id belongs to
# clipId : clipCategoryNumbers
def makeBelongsTo():
    belongsTo = defaultdict(list)
    with open(PROJECT_DIR + '\similar-staff-picks-challenge-clip-categories.csv',newline='') as csvfile1:
        reader = csv.reader(csvfile1)
        for i, row in enumerate(reader):
            if isinstance(row[1], str):
                strCats = row[1].split(", ")
                intCats = [int(c) for c in strCats]
                belongsTo[row[0]] = intCats
            else:
                belongsTo[row[0]] = [row[1]]

    return belongsTo

# Make a dictionary to give the category names of each category_id
# categoryId : categoryName
def makeCategoryNamesDict():
    categories = defaultdict(int)
    with open(PROJECT_DIR + '\similar-staff-picks-challenge-categories.csv', newline='') as categoriesFile:
        reader = csv.reader(categoriesFile)
        for i, row in enumerate(reader):
            categories[row[0]] = row[2]
    return categories

# Make a dictionary to get the category names for each category id
# categoryId : comma separated category list
def getCategoryNames(categoryIds):
    catNames = [categories[str(catid)] for catid in categoryIds]
    return catNames

# Make 3 dictionaries to get the titles, captions and image information for each clipId
def makeTitlCapImg():
    titles = defaultdict(str)
    captns = defaultdict(str)
    image = defaultdict(str)
    with open(PROJECT_DIR + '\similar-staff-picks-challenge-clips.csv', newline='', encoding="utf8") as csvfile3:
        reader = csv.reader(csvfile3)
        for row in reader:
            titles[row[1]] = row[2]
            captns[row[1]] = row[3]
            image[row[1]] = row[11]
    return titles, captns, image

# Get the categories of maximum possible clip_ids
def getMaxPossibleCategories():
    labelled = []
    with open(PROJECT_DIR + '\similar-staff-picks-challenge-clips.csv', newline='', encoding="utf8") as csvfile2:
        reader = csv.reader(csvfile2)
        for row in reader:
            if belongsTo.get(row[1]):
                categoryNames = getCategoryNames(belongsTo[row[1]])
            else:
                categoryNames = []

            title = row[2]
            captions = row[3].replace('\r\n', ' ')

            # Append all the words from the title, captegory names and captions for vectorization
            toVectorize = []
            if len(categoryNames) > 0:
                toVectorize.extend(categoryNames)
            toVectorize.append(title)
            toVectorize.append(captions)

            toVectorize = ' '.join(toVectorize)

            # Get the stop words
            stop_words = set(stopwords.words('english'))

            # Tokenize words
            word_tokens = word_tokenize(toVectorize)

            # Get all the words to lower case, remove stop words and punctuations
            filtered_sentence = [w.lower() for w in word_tokens if not w in stop_words and w.isalpha()]

            # Tag each sentence with this clipId
            labelled.append(TaggedDocument(filtered_sentence, [row[1]]))
    return labelled

belongsTo = makeBelongsTo()
categories = makeCategoryNamesDict()
titles, captns, image = makeTitlCapImg()
taggedDoc = getMaxPossibleCategories()







# print(similar_doc)