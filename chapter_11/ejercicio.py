import re 
res=0
hand = open('chapter_11/regex_sum_188766.txt')
#hand = open('chapter_11/regex_sum_42.txt')
for line in hand:
	y = re.findall('[0-9]+',line)
	if len(y) != 0:
		y = [int(i) for i in y]
		res = res+sum(y)
print res	
