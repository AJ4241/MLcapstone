# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import pickle
import json

oop = pd.read_csv('otra.csv')
tfidf = TfidfVectorizer(stop_words='english')
oop.set_index(pd.Index(range(0,len(oop),1)))

tfidf_matrix = tfidf.fit_transform(oop['Description'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indxs = pd.Series(oop.index, index = oop['Name']).drop_duplicates()

def what2read(title,cosine_sim=cosine_sim):
  #title = input("Enter book title")
  indx = indxs[title]
  similarity = []
  for e in cosine_sim[indx]:
    sum = [e]
    similarity.append(sum)
  for d in range(len(similarity)):
    similarity[d].append(d)
  similarity = sorted(similarity, key=lambda x:x[0], reverse=True)
  for f in range(len(similarity)):
    similarity[f].append(oop['Name'].iloc[similarity[f][1]])
    similarity[f].append(oop['Rating'].iloc[similarity[f][1]])
  yurr = otherfun(similarity)
  return(yurr)

def otherfun(books):
  dede = []
  for i in books:
    if (i[0]>0.05 and i[0]<0.9):
      dede.append(i)
  keke = [0, 1, 2]
  otherL = [dede[g] for g in keke]
  pogo = []
  for q in dede:
    if q!=otherL[0] and q!=otherL[1] and q!=otherL[2]:
      pogo.append(q)
  algo = sorted(pogo, key=lambda x:x[3], reverse=True)
  hehe = [0,1]
  jkjk = [algo[f] for f in hehe]
  aye = join2(otherL, jkjk)
  return(aye)

def join2(a, b):
  a.extend(b)
  shure = []
  for j in a:
    shure.append(j[2])
  return(shure)

bookL = open("./TestData.json")
after = json.load(bookL)
mon = after[0]
jol = mon['title']

book = what2read(jol)

sumfile = open("w2r.pkl","wb")
pickle.dump(book,sumfile)
sumfile.close()

sumfile2 = open("w2r.pkl","rb")
MLmodel = pickle.load(sumfile2)
sumfile2.close()
