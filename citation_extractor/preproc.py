# -*- coding: utf-8 -*-
# author: Matteo Romanello, matteo.romanello@gmail.com

import logging

sample = """
In Statius ' « Achilleid » (2, 96-102) Achilles describes his diet of wild animals in infancy,
which rendered him fearless and may indicate another aspect of his character - a tendency toward aggression and anger.
The portrayal of angry warriors in Roman epic is effected for the most part not by direct descriptions but indirectly,
by similes of wild beasts (e.g. Vergil, Aen. 12, 101-109 ; Lucan 1, 204-212 ; Statius, Th. 12, 736-740 ; Silius 5, 306-315).
These similes may be compared to two passages from Statius (Th. 1, 395-433 and 8, 383-394) that portray the onset of anger in direct narrative.
Analysis of these passages demonstrates that the concept of « ira » in epic takes its moral aspect from the context.
"""

global logger
logger = logging.getLogger("CREX.preprocessing")

def detect_language(text):
	"""
	Detect language of a notice by using the module guess_language.
	The IANA label is returned.
	
	Args:
		text:
			the text whose language is to be detected
	Returns:
		lang:
			the language detected
	"""
	import guess_language
	try:
		lang = guess_language.guessLanguage(text)
		return lang
	except Exception,e:
		print "lang detection raised error \"%s\""%str(e)

def create_tagger(lang_code,inp_enc="utf-8",out_enc="utf-8",abbrev_file="/Users/56k/phd/code/APh/corpus/extra/abbreviations.txt",treetagger_dir="/Applications/treetagger/"):
	"""docstring for create_tagger"""
	import treetaggerwrapper
	return treetaggerwrapper.TreeTagger(TAGLANG=lang_code,TAGDIR=treetagger_dir,TAGINENC=inp_enc,TAGOUTENC=out_enc,TAGABBREV=abbrev_file)

def tokenize_and_POStag(treetagger,text):
	"""
	Performs the tokenization and POS tagging of the input text.
	
	"""
	temp = treetagger.TagText(text)
	return [tuple(line.split('\t'))[:2] for line in temp]

def create_instance_tokenizer(train_dirs=[("/Users/56k/phd/code/APh/corpus/txt/",'.txt'),]):
	from nltk.tokenize.punkt import PunktSentenceTokenizer
	import glob
	import os
	import re
	import codecs
	sep = "\n"
	train_text = []
	for dir in train_dirs:
		train_text += [codecs.open(file,'r','utf-8').read() for file in glob.glob( os.path.join(dir[0], '*%s'%dir[1]))]
	return PunktSentenceTokenizer(sep.join(train_text))


if __name__ == "__main__":
	"""
	# this code process the APh corpus devset dynamically (sentence tokenization -> lang detection -> tokenization and POS tagging)
	
	import os, glob, codecs
	dir = ('/Users/56k/Documents/Research/CCH_PhD/ResearchProject/code/APh/corpus/devset','.txt')
	texts = [codecs.open(file,'r','utf-8').read() for file in glob.glob( os.path.join(dir[0], '*%s'%dir[1]))]
	sent_tokenizer = create_instance_tokenizer()
	for text in texts[:10]:
		res = [tokenize_and_POStag(sent, detect_language(sent)) for sent in sent_tokenizer.tokenize(text)]
		print res
	
	# at this point we should extract the NEs and write output to IOB files
	
	"""
	
	"""
	# this snippet will come in handy later
	
	input = [[[token[0] for token in instance] for instance in self.test_instances]]
	if(len(self.test_instances[0][0]) > 2):
		self.label_index = 2 # the last one is the label
		legacy_features = [[("z_POS",token[1]) for token in instance] for instance in self.test_instances]
		output = eng.extract(input,[legacy_features])
	"""