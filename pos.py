import nltk

lines = nltk.word_tokenize("One shouldn't disobey the law")

poss = nltk.pos_tag(lines)

print(poss)
