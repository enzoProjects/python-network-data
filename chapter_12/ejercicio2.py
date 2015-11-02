__author__ = 'springfield'

import urllib
from BeautifulSoup import*

#abro documento del internet
html = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Davi.html').read()
#beatiful soup solo crea un objeto genial al cual dsp le puedo pedir qe busque en el html <a ..... >
soup = BeautifulSoup(html)

for x in range(7):
    tags = soup('a')
    link = tags[17].get('href')
    html = urllib.urlopen(link).read()
    soup = BeautifulSoup(html)

print tags[17].contents[0]


