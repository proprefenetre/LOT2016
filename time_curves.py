#!/usr/bin/python
#-*- coding: utf-8 -*- 

import os.path
import glob
from itertools import takewhile
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import pairwise_distances
import pandas as pd
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

# {"data":    [    {"timelabels":    [..., ..., ...,], "name":"chain-letters"}    ], "distance matrix": [[..., ..., ...,]]    }

with open("data/luck-chain-letters.json", "w") as out:
    json.dump(output, out)

