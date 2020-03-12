import spacy
import json
import sys
import os

# python 2 or 3 compatibility selector
if sys.version_info[0] >= 3:
    unicode = str

# open the settings
with open( "settings.json", "r") as data:
	settings 	= json.load(data)
	cache_path 	= settings['cache_path']

# dict to cache the similarity of two words/phrases
with open(os.path.join(cache_path,'similarity_dict.json'), "r") as data:
	similarity_dict = json.load(data)

# instantiate spacy with the largest model
nlp = spacy.load('en_vectors_web_lg')

# save the label_dict
def save_cached_data():
	with open(os.path.join(cache_path,'similarity_dict.json'), 'wb') as outfile:
		outfile.write(json.dumps(similarity_dict, separators=(',',':')).encode('utf8'))

#calculate the similarity of the words using word2vec
def similarity_word2vec(question_word, candidate):
	if not candidate or candidate == "":
		return 0
	
	if similarity_dict.get(question_word) != None and similarity_dict.get(question_word).get(candidate) != None:
		return similarity_dict[question_word][candidate]

	nlp_qestion_word = nlp(unicode(question_word.encode("utf-8"),encoding="utf-8"))
	nlp_candidate = nlp(unicode(candidate.encode("utf-8"),encoding="utf-8"))
		
	if not nlp_candidate or not nlp_qestion_word:
		return 0
	if not nlp_candidate.vector_norm or not nlp_qestion_word.vector_norm:
		return 0

	similarity = nlp_qestion_word.similarity(nlp_candidate)
	similarity_dict[question_word] = {candidate: similarity}
	return similarity
	