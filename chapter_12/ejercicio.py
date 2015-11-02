__author__ = 'springfield'

import urllib
from BeautifulSoup import*

#abro documento del internet
html = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_188771.html').read()
#beatiful soup solo crea un objeto genial al cual dsp le puedo pedir qe busque en el html <span ..... >
soup = BeautifulSoup(html)
tags = soup('span')

#sumo su contenido (listo por comprension)
print sum([int(tag.contents[0]) for tag in tags])