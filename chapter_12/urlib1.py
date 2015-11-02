__author__ = 'springfield'

import urllib
#fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
larebelion = urllib.urlopen('http://www.samaelgnosis.net/libros/txt/gran_rebelion.txt')
#for line in fhand:
#    print line.strip()


# al parecer como en c++ cuando uso algo de fhand (file handler) se borra de memoria

frequencies = dict()
for line in larebelion:
    line.strip()
    words=line.split()
    for word in words:
        frequencies[word] = frequencies.get(word,0) +1
print frequencies