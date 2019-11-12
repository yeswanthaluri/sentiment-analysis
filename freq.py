import collections

wordcount = collections.Counter()
with open("hamlet.txt") as file:
    for line in file:
        wordcount.update(line.split())

print (wordcount)