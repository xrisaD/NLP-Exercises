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
from pprint import pprint

#downloads
nltk.download('punkt')
nltk.download('gutenberg')
nltk.download('stopwords')

book = gutenberg.raw('melville-moby_dick.txt')
#book = gutenberg.raw('shakespeare-caesar.txt')

#PART1
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

#PorterStemmer:removing the commoner morphological and inflexional endings from words in English
#also delete stopwords
stemmer = PorterStemmer()
training_stems = [stemmer.stem(w) for w in words if w not in stopwords.words('english')]

#create vocabulary with words that occur more than 10 times
count = nltk.FreqDist(training_stems)
vocabulary = [w  for w in count if count[w]>10]
#pprint(vocabulary)

#replace other words with a special token *UNK*
def replaceWithUNK(sentences):
  done_sentences = []
  for s in sentences:   
    done_sent = [stemmer.stem(w) if (stemmer.stem(w) in vocabulary) else "*UNK*" for w in s]
    done_sentences.append(done_sent)
  return done_sentences
#do the replace
done_training_sentences = replaceWithUNK(training_sentences)
done_development_sentences = replaceWithUNK(development_sentences)
done_test_sentences = replaceWithUNK(test_sentences)

#Bigram and trigram language model for word sequences
def createBiTrigrams(sentences):
  bigram_counter = Counter()
  trigram_counter = Counter()
  for sent in sentences:
    bigram_counter.update([gram for gram in ngrams(sent, 2, pad_left=True, pad_right=True,left_pad_symbol='<start>',right_pad_symbol='<end>') ])
    trigram_counter.update([gram for gram in ngrams(sent, 3, pad_left=True, pad_right=True,left_pad_symbol='<start>',right_pad_symbol='<end>') ])
  return (bigram_counter, trigram_counter)
#create model
(bigram_counter, trigram_counter) = createBiTrigrams(done_training_sentences)

#PART 2
