__author__ = 'springfield'
from operator import itemgetter, attrgetter
import urllib
from BeautifulSoup import*

#fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
hunger = urllib.urlopen('https://archive.org/stream/Book1TheHungerGames/Book%201%20-%20The%20Hunger%20Games_djvu.txt')
#for line in fhand:
#    print line.strip()

# al parecer como en c++ cuando uso algo de fhand (file handler) se borra de memoria

#frecuencia de palabras
"""
frequencies = dict()
for line in hunger:
    unwanted_chars = "\".,-_!?</>/= "
    words=line.split()
    for raw_word in words:
        raw_word = raw_word.lower()
        word = raw_word.strip(unwanted_chars)
        frequencies[word] = frequencies.get(word,0) +1
print sorted(frequencies, key=frequencies.__getitem__, reverse=True)
"""

#frecuencia de letras
"""
s=0

frequencies = dict()
for line in hunger:
    unwanted_chars = "\"\'.,-_!?</>/\=[]{ }\xab\xc2 "
    words=line.split()
    for raw_word in words:
        raw_word = raw_word.lower()
        word = raw_word.strip(unwanted_chars)
        word = list(word)
        for letter in word:
            frequencies[letter] = frequencies.get(letter,0) +1
            s = s+1
frec =[()]
tot =0
for i in frequencies.items():
    tot = tot+float(i[1])/s*100
    frec.append((float(i[1])/s*100,i[0]))

sortedFrec = sorted(frec,reverse=True)
for i in sortedFrec:
    print 'letra: ' + str(i[1]) + ' aparece :' +str(i[0]) +' % '
"""

