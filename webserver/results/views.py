from django.shortcuts import render_to_response
from gensim.models.doc2vec import Doc2Vec
import json
import sys
import os
PROJECT_DIR = os.getcwd()
sys.path.insert(0, PROJECT_DIR)
from dataReady2 import belongsTo, categories, titles, captns, image
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render_to_response('showResults.html')

def compute(request):
    # Load the saved model
    try:
        model = Doc2Vec.load("ClipModel")
        clipid = request.GET.get('clipid', '')

        results = []
        # Find 10 most similar clips
        similar_doc = model.docvecs.most_similar(positive=[clipid], topn=10)
        for simDoc in similar_doc:
            clipId = simDoc[0]
            doc = {}
            doc['id'] = clipId
            catNames = [categories[str(catid)] for catid in belongsTo[clipId]]
            doc['title'] = titles[clipId]
            doc['captions'] = str(captns[clipId]).replace('\r\n', ' ')
            doc['categories'] = catNames
            doc['image'] = image[clipId]
            results.append(doc)
#             jresults = json.dumps(results, indent=4)
        return render_to_response('viewResults.html', {'result' : results})

    except Exception as html:
        html = "<html> <body>Clip ID not found in database </body></html>"
        return HttpResponse(html)
