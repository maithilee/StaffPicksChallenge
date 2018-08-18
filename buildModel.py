from gensim.models.doc2vec import Doc2Vec

from dataReady2 import taggedDoc

num_features = 200
min_word_count = 1
num_workers = 4
context = 5
iteration = 7

model = Doc2Vec(taggedDoc, workers=num_features, min_count=min_word_count, vector_size=num_features, window=context, epochs=iteration)
model.save('ClipModel')
print ("Model saved!")