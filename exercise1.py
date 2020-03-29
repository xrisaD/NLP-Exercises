#!pip install -U nltk
import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
import math 

from nltk.tokenize import WhitespaceTokenizer
import collections
from nltk.stem import PorterStemmer

from nltk.corpus import stopwords
from collections import Counter
from nltk.util import ngrams

#downloads
nltk.download('punkt')
nltk.download('gutenberg')
nltk.download('stopwords')

book = gutenberg.raw('melville-moby_dick.txt')
#book = gutenberg.raw('shakespeare-caesar.txt')

sentences = sent_tokenize(book)
length = len(sentences)
training_set = sentences[0 : math.ceil( length*(80/100))]
development_set = sentences[math.ceil( length*(80/100)) : math.ceil( length*(90/100))]
test_set = sentences[math.ceil( len(sentences)*(90/100))]

#Create dictionary from training set:
#Tokenization
words=[]
training_sentences = []
development_sentences = []
test_sentences = []
whitespace_wt = WhitespaceTokenizer()
for i, j , k in zip(training_set, development_set, test_set):
  training_s = whitespace_wt.tokenize(i)
  development_s = whitespace_wt.tokenize(j)
  test_s = whitespace_wt.tokenize(k)
  training_sentences.append(training_s)
  development_sentences.append(development_s)
  test_sentences.append(test_s)
  #save training words, use them later to create vocabulary
  for w in training_s:
    words.append(w)  
