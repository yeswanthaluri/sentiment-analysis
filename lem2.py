import nltk
from nltk.corpus import udhr

udhr = nltk.corpus.udhr.words('English-Latin1')

for t in udhr[:20]:
	WNlemma = nltk.WordNetLemmatizer()
	lem=WNlemma.lemmatize(t)
	print(lem)