# -*- coding: utf-8 -*-
"""ContentFilter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DzxOQJVzihQax0uI7-NvWARBE311xUdc

## **Code to reduce size of dataset (by removing unnecessary columns and only keeping books that are in english)**
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


dfContent = pd.read_csv("book1000k-1100k.csv")

dropContent = ['PublishMonth','PublishDay','Count of text reviews','Id','RatingDist5','RatingDist4','RatingDist3','RatingDist2','RatingDist1','RatingDistTotal','Count of text reviews','ISBN']

dfContent = dfContent.drop(dropContent, axis=1)
print(dfContent)

something = dfContent[dfContent['Language'].str.contains('eng|en-US|en-GB',case=False, na=False)]
print(something)

again = something[something.Description != ""]


"""## **Code to vectorize text descriptions**"""

tfidf = TfidfVectorizer(stop_words='english')

again['Description'] = again['Description'].fillna('')
again = again[again.Description != '']
again.to_csv('otra.csv',index=False)

oop = pd.read_csv('otra.csv')
tfidf_matrix = tfidf.fit_transform(oop['Description'])
tfidf_matrix.shape

tfidf.get_feature_names_out()[7000:7010]

from sklearn.metrics.pairwise import linear_kernel

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

cosine_sim.shape

cosine_sim[1]

indxs = pd.Series(oop.index, index = oop['Name']).drop_duplicates()

indxs[:10]

"""## **Write a function that's responsible for finding the most similar books to a given title**"""

def what2read(title, cosine_sim=cosine_sim):
  indx = indxs[title]
  similarity = list(enumerate(cosine_sim[indx]))
  similarity = sorted(similarity, key=lambda x:x[1], reverse=True)
  similarity = similarity[1:11]
  movIndx = [i[0] for i in similarity]
  return oop['Name'].iloc[movIndx]

what2read('The Wizard of Oz')