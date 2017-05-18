#!/usr/bin/env python3

import sys
import json
from ngramiter import CorpusNgramIterator
from trainvec import trainEmbeddings

if __name__ == "__main__":
	#ngramIter = CorpusNgramIterator(sys.argv[1], 1024, minCounts = [5, 80, 100])
	ngramIter = CorpusNgramIterator(sys.argv[1], 1024, minCounts = [5, 80], stopAtNCorpusPasses = 15)
	#ngramIter = CorpusNgramIterator(sys.argv[1], 1024, minCounts = [5])
	
	embeddings = trainEmbeddings(ngramIter.getVocSize(), ngramIter)
	
	with open(sys.argv[2], 'w') as outFh:
		json.dump({ 'embeddings': embeddings.tolist(), 'dicts': ngramIter.getDicts() }, outFh)
