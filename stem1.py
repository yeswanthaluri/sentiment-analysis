import nltk

input1 = "List listed lists listing listings"
words1 = input1.lower().split(' ')
print(words1)

for t in words1:
	porter = nltk.PorterStemmer()
	port = porter.stem(t)
	print(port)