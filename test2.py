import collections
import json
import pprint
import sys
from gensim.models.doc2vec import Doc2Vec
from dataReady2 import belongsTo, categories, titles, captns, image

model = Doc2Vec.load("ClipModel")
inputClip = sys.argv[1]

# Make results.json
# clipIds = inputClip.strip('[]').split(', ')
# results = []
# with open('results.json', 'w') as fp:
#     for clip in clipIds:
#         fp.write("10 SIMILAR DOCS FOR CLIP ID: " + clip + "\n")
#         similar_doc = model.docvecs.most_similar(positive=[clip], topn=10)
#         # print(similar_doc)
#         for simDoc in similar_doc:
#             clipId = simDoc[0]
#             doc = {}
#             doc['id'] = clipId
#             catNames = [categories[str(catid)] for catid in belongsTo[clipId]]
#             doc['title'] = titles[clipId]
#             doc['captions'] = captns[clipId].replace('\r\n', ' ')
#             doc['categories'] = catNames
#             doc['image'] = image[clipId]
#             jdoc = json.dump(doc, fp)
#             fp.write('\n\n')
#             # results.append(jdoc)
#             # jresults = json.dumps(results)

results = []
try:
    similar_doc = model.docvecs.most_similar(positive=[inputClip], topn=10)
    print ("10 most similar video clips for clip %s are: " %inputClip)
    for simDoc in similar_doc:
        clipId = simDoc[0]
        doc = collections.OrderedDict()
        doc['id'] = clipId
        catNames = [categories[str(catid)] for catid in belongsTo[clipId]]
        doc['title'] = titles[clipId]
        doc['captions'] = captns[clipId].replace('\r\n', ' ')
        doc['categories'] = catNames
        doc['image'] = image[clipId]
        results.append(doc)

    jresults = json.dumps(results)
    pprint.pprint(jresults)
except:
    print ("Clip ID not found in database")
    
