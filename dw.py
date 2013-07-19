#coding=utf-8

#filename = input("FILENAME:")
f = open('sample.txt','r')
try:
	words = []
	sentence = []
	for x in f:
		sentence.append(x)
	#sentence.pop()

	def dellines(a):
		i = 0
		while True:
			if i == len(a):
				break
			if not a[i].isalpha():
				del a[i]
				continue
			else:
				i = i + 1
		return a



	for i in range(len(sentence)):
		temp = sentence[i].split()
		j = 0
		while True:
			temp[j] = temp[j].strip('.,:?!/(){}[]"\'\\')
			temp[j] = temp[j].strip('.,:?!/(){}[]"\'\\')
			j = j + 1
			if j == len(temp):
				break
		for k in temp:
			words.append(k.lower())

	words = list(set(words)) #去掉重复元素
	words = dellines(words) #去掉特殊符号
	words.sort()		#排序

	print(len(words))  #3445个单词
	print(len(sentence)) #1450个句子

	wins = [[0 for i in range(len(words))]for j in range(len(sentence))]

	##for i in sentence:
	#	for j in words:
	#		if j in i:
	#			wins[sentence.index(i)][words.index(j)] = 1
	
	for st in sentence:
		tp = st.split()
		length = len(tp)
		k = 0
		while k < length:
			tp[k] = tp[k].strip('.,:?!/(){}[]"\'\\')
			k += 1
		for i in tp:
			if i.lower() in words:
				wins[sentence.index(st)][words.index(i.lower())] = 1
	#print len(wins)
	#count = 0
	#for i in wins[2]:
	#	count += i
	#print count

	#print words
	#rint wins[0]
	#print wins[1]
	#print wins[2]
	#print tp
	#import sys
	g = open('test.txt','w')
	for i in wins:
		print >>g,i

finally:
	f.close()
