#A small english lexicon
#use: wordNet
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

def listToString(s):
    string = ""   
    for word in s:  
        string += word + ", "  
    return string  
while(True):
  print("Enter a word or enter 'q' to quit.")
  word = input()
  if(word=='q'):
    break
  synsets = wn.synsets(word)
  if(synsets is not None and len(synsets)>0):
    for synset in synsets:
      print("Definition: " + synset.definition())
      synonyms = listToString(synset.lemma_names())
      print("Synonyms : " + synonyms[:len(synonyms)-2])
      examples = synset.examples()
      if(examples is not None and len(examples)>0):
        print("Examples:")
        for i in synset.examples():
          print(i)
      print()
    print()
  else:
    print("This word does not exist.")
  print()
