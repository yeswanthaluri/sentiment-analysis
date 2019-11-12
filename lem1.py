import nltk
from nltk.corpus import udhr

udhr = nltk.corpus.udhr.words('English-Latin1')

for t in udhr[:20]:
	porter = nltk.PorterStemmer()
	port=porter.stem(t)
	print(port)
