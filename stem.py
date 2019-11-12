import nltk

file = open("hamlet.txt", "r")
lines = file.readlines()

porter = nltk.PorterStemmer()
[porter.stem(t) for t in lines]

print (lines)