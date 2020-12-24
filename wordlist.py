# [len]--1 chars--2 name_of_file--3
from itertools import permutations
import sys
import pdb
import os
filename = os.getenv('HOME') + '/' + sys.argv[3]
b = []

while int(sys.argv[1])<1:
	print('Passwords of 0 length cannot be formed')
else:
	file = open(filename,'w')
	words = sys.argv[2].split(sep = ',')
	password = ''
	for word in words:
		p = permutations(word,int(sys.argv[1]))
		for i in p:
			b = list(i)
			for j in b:
				password += j
			file.writelines(password + '\n')
			password = ''

file.close()
print('The file ' + sys.argv[3] + ' has been created')
