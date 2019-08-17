#!/usr/bin/python

import sys
counts = dict( )
for line in sys.stdin:
	data = line.strip().split("\t")
	for word in data:
		counts[word] = counts.get(word, 0) +1

target_words = ['Sydney', 'Melbourne', 'Brisbane', 'Canberra', 'Perth', 'Adelaide']
for city, count in counts.items():
	if city in target_words:
		print("{0}\t{1}".format(city, count))