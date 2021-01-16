# [type of pass]--1 [len]--2 chars--3 name_of_file--4
from itertools import product,permutations,combinations,combinations_with_replacement
import sys
import os

filename = 'C:\\Users\\Gaurav\\Desktop\\New folder\\' + sys.argv[4]
b = []

def prod():     #pr with replacement
        file = open(filename,'w')						
        word = sys.argv[3]
        password =''
        p = product(word,repeat = int(sys.argv[2]))
        for i in p:
                b = list(i)
                for j in b:
                        password += j
                file.writelines(password + '\n')
                password = ''
        file.close()

def perm():     #p factorial of length
	file = open(filename,'w')						
	word = sys.argv[3]
	password = ''
	p = permutations(word,r = int(sys.argv[2]))		
	for i in p:
		b = list(i)
		for j in b:
			password += j
		file.writelines(password + '\n')
		password = ''
	file.close()

def comb():     #c possible combiantions
        file = open(filename,'w')
        word = sys.argv[3]
        password = ''
        p = combinations(word,r = int(sys.argv[2]))
        for i in p:
                b = list(i)
                for j in b:
                        password += j
                file.writelines(password + '\n')
                password = ''
        file.close()

def comb_rep(): #cr using law of multiplication
        file = open(filename,'w')
        word = sys.argv[3]
        password = ''
        p = combinations_with_replacement(word,r = int(sys.argv[2]))
        for i in p:
                b = list(i)
                for j in b:
                        password += j
                file.writelines(password + '\n')
                password = ''
        file.close()
			
while int(sys.argv[2])<1:
        print('Passwords of 0 length cannot be formed')
else:
        while sys.argv[1] not in ['--pr','--p','--c','--cr']:
        	print('Re-run the script and pass the type of wordlist you want')
        else:
                if sys.argv[1] == '--pr':
                        prod()
                elif sys.argv[1] == '--p':
                        perm()
                elif sys.argv[1] == '--c':
                        comb()
                elif sys.argv[1] == '--cr':
                        comb_rep()

g = open(filename,'r')
length = len(g.readlines())
print('The file ' + sys.argv[4] + ' has been created with ',length,' passwords')
