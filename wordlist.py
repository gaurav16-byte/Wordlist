# [type of pass]--1 [len]--2 chars--3 name_of_file--4 -t --5 pat_only_text??? or ???text --6
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

def prod_pat1():     #pr with replacement
        file = open(filename,'w')						
        word = sys.argv[3]
        password =''
        p = product(word,repeat = length)
        for i in p:
                b = list(i)
                for j in b:
                        password += j
                file.writelines(keyword + password + '\n')
                password = ''
        file.close()

def perm_pat1():     #p factorial of length
	file = open(filename,'w')						
	word = sys.argv[3]
	password = ''
	p = permutations(word,r = length)		
	for i in p:
		b = list(i)
		for j in b:
			password += j
		file.writelines(keyword + password + '\n')
		password = ''
	file.close()

def comb_pat1():     #c possible combiantions
        file = open(filename,'w')
        word = sys.argv[3]
        password = ''
        p = combinations(word,r = length)
        for i in p:
                b = list(i)
                for j in b:
                        password += j
                file.writelines(keyword + password + '\n')
                password = ''
        file.close()

def comb_rep_pat1(): #cr using law of multiplication
        file = open(filename,'w')
        word = sys.argv[3]
        password = ''
        p = combinations_with_replacement(word,r = length)
        for i in p:
                b = list(i)
                for j in b:
                        password += j
                file.writelines(keyword + password + '\n')
                password = ''
        file.close()

def prod_pat2():     #pr with replacement
        file = open(filename,'w')						
        word = sys.argv[3]
        password =''
        p = product(word,repeat = length)
        for i in p:
                b = list(i)
                for j in b:
                        password += j
                file.writelines(password + keyword + '\n')
                password = ''
        file.close()

def perm_pat2():     #p factorial of length
	file = open(filename,'w')						
	word = sys.argv[3]
	password = ''
	p = permutations(word,r = length)		
	for i in p:
		b = list(i)
		for j in b:
			password += j
		file.writelines(password + keyword + '\n')
		password = ''
	file.close()

def comb_pat2():     #c possible combiantions
        file = open(filename,'w')
        word = sys.argv[3]
        password = ''
        p = combinations(word,r = length)
        for i in p:
                b = list(i)
                for j in b:
                        password += j
                file.writelines(password + keyword + '\n')
                password = ''
        file.close()

def comb_rep_pat2(): #cr using law of multiplication
        file = open(filename,'w')
        word = sys.argv[3]
        password = ''
        p = combinations_with_replacement(word,r = length)
        for i in p:
                b = list(i)
                for j in b:
                        password += j
                file.writelines(password + keyword + '\n')
                password = ''
        file.close()

try:
        id(sys.argv[5])
except IndexError:
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
else:
        while sys.argv[5] not in '--t--T':
                print('Invalid paramater for pattern check out the changelog...')
        else:
                pattern = sys.argv[6]
                if pattern.find('?') == 0:
                        length = pattern.rfind('?') + 1
                        keyword = pattern[pattern.rfind('?') + 1:len(pattern)]
                        while int(sys.argv[2])<1:
                                print('Passwords of 0 length cannot be formed')
                        else:
                                while sys.argv[1] not in ['--pr','--p','--c','--cr']:
                                        print('Re-run the script and pass the type of wordlist you want')
                                else:
                                        if sys.argv[1] == '--pr':
                                                prod_pat2()
                                        elif sys.argv[1] == '--p':
                                                perm_pat2()
                                        elif sys.argv[1] == '--c':
                                                comb_pat2()
                                        elif sys.argv[1] == '--cr':
                                                comb_rep_pat2()
                else:
                        keyword = pattern[:pattern.find('?')]
                        length = len(pattern) - len(keyword)
                        while int(sys.argv[2])<1:
                                print('Passwords of 0 length cannot be formed')
                        else:
                                while sys.argv[1] not in ['--pr','--p','--c','--cr']:
                                        print('Re-run the script and pass the type of wordlist you want')
                                else:
                                        if sys.argv[1] == '--pr':
                                                prod_pat1()
                                        elif sys.argv[1] == '--p':
                                                perm_pat1()
                                        elif sys.argv[1] == '--c':
                                                comb_pat1()
                                        elif sys.argv[1] == '--cr':
                                                comb_rep_pat1()
finally:
        g = open(filename,'r')
        length = len(g.readlines())
        print('The file ' + sys.argv[4] + ' has been created with ',length,' passwords')
