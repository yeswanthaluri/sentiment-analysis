import nltk
from nltk.corpus import udhr

udhr = nltk.corpus.udhr.words('English-Latin1')

print (udhr[:20])

