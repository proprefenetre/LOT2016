#!/usr/bin/python
#-*- coding: utf-8 -*- 

import os.path
import glob
from itertools import takewhile
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import pairwise_distances
import  pandas as pd
import json

fnames1 = glob.glob("data/luck-chain-letters/chain-letters/*.txt")

vectorizer = CountVectorizer(input='fname')

x = vectorizer.fit_transform(fnames1)

dm = pairwise_distances(x, metric='cosine')

#os.path.basename(fnames1[0])
def fname2date(fn):
    fn = os.path.basename(fn)
    date = ''.join(takewhile(lambda c: c.isdigit() or c == '-', fn[2:]))
    return str(pd.datetools.to_datetime(date)) + '.0'

dates = [fname2date(fname) for fname in fnames1]

output = {"distance matrix":dm.tolist(), "data": [{"name":"chain-letters",
"timelabels": dates}]}

with open("data/luck-chain-letters.json", "w") as out:
    json.dump(output, out)

#fnames = ["data/luck-chain-letters/chain-letters/" + f for f in os.listdir("data/luck-chain-letters/chain-letters/") if not f.startswith('.')]

#text = []
#for f in fnames:
#    with open(f, 'r') as letter:
#        text.append(letter.read())
#
## vector representations:
## create a vector for each text. make sure the vectors are of equal length!
#
#C = []
#for item in text:
#    C.extend(item)
#    
#print(len(C))
#

# see ipython history!

