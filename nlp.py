from __future__ import print_function, division
from future.utils import iteritems
from builtins import range

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from wordcloud import WordCloud

# Load dataset: https://www.kaggle.com/uciml/sms-spam-collection-dataset
df = pd.read_csv('dataset/spam.csv', encoding='ISO-8859-1')

# Remove garbage and give columns meaningful names
df = df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
df.columns = ['labels', 'data']

# Add a key for binary labels instead of 'ham' and 'spam'
# Pandas map, returns ['labels', 'data', 'b_labels']
# Map transforms ham and spam into 0s and 1s
df['b_labels'] = df['labels'].map({'ham': 0, 'spam': 1})

# Pandas.DataFrame.as_matrix, returns numpy array
Y = df['b_labels'].as_matrix()

# Try multiple ways of calculating features
count_vectorizer = CountVectorizer(decode_error='ignore')
X = count_vectorizer.fit_transform(df['data'])

# Split up the data
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.33)

# Create model, train, and print scores
model = MultinomialNB()
model.fit(Xtrain, Ytrain)

print('Train score: ', model.score(Xtrain, Ytrain))
print('Test score: ', model.score(Xtest, Ytest))
