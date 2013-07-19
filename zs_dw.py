#coding=utf-8
import re
regex = re.compile(ur'[^\u4e00-\u9fa5a-zA-Z0-9\'\]')

#filename = input("FILENAME:")
f1 = open('joshua.result','r')
f2 = open('moses.result','r')
f3 = open('sample.txt','r')
g1 = open('test1.txt','w')
g2 = open('test2.txt','w')
g3 = open('test3.txt','w')
try:
    words = []
    sentence1 = []
    sentence2 = []
    sentence3 = []
    for x in f1:
        sentence1.append(x)
    for x in f2:
        sentence2.append(x)
    for x in f3:
        sentence3.append(x)
    sentence = sentence1 + sentence2 + sentence3

    def dellines(a):
        i = 0
        while True:
            if i == len(a):
                break
            if regex.match(a[i].decode('utf8')) != None:
                del a[i]
                continue
            else:
                i = i + 1
        return a



    for i in range(len(sentence)):
        temp = sentence[i].split()
        j = 0
        while j < len(temp):
            temp[j] = temp[j].strip('.,:?!/(){}[]"\'\\')
            j = j + 1
        for k in temp:
            words.append(k.lower())

    words = list(set(words)) #去掉重复元素
    words = dellines(words) #去掉特殊符号
    words.sort()        #排序

    print(len(words))  #3445个单词
    print(len(sentence)) #1450个句子

    anal1 = [['0' for i in range(len(words))]for j in range(len(sentence1))]
    anal2 = [['0' for i in range(len(words))]for j in range(len(sentence2))]
    anal3 = [['0' for i in range(len(words))]for j in range(len(sentence3))]

    ##for i in sentence:
    #   for j in words:
    #       if j in i:
    #           wins[sentence.index(i)][words.index(j)] = 1

    for st in sentence1:
        tp = st.split()
        length = len(tp)
        k = 0
        while k < length:
            tp[k] = tp[k].strip('.,:?!/(){}[]"\'\\')
            k += 1
        for i in tp:
            if i.lower() in words:
                anal1[sentence1.index(st)][words.index(i.lower())] = '1'

    for st in sentence2:
        tp = st.split()
        length = len(tp)
        k = 0
        while k < length:
            tp[k] = tp[k].strip('.,:?!/(){}[]"\'\\')
            k += 1
        for i in tp:
            if i.lower() in words:
                anal2[sentence2.index(st)][words.index(i.lower())] = '1'

    for st in sentence3:
        tp = st.split()
        length = len(tp)
        k = 0
        while k < length:
            tp[k] = tp[k].strip('.,:?!/(){}[]"\'\\')
            k += 1
        for i in tp:
            if i.lower() in words:
                anal3[sentence3.index(st)][words.index(i.lower())] = '1'


    '''print len(anal1)
    count = 0
    for i in anal1[2]:
        count += i
    print count'''

    #print words
    #rint wins[0]
    #print wins[1]
    #print wins[2]
    #print tp
    #import sys
    for i in anal1:
        print >>g1,' '.join(i)
    for i in anal2:
        print >>g2,' '.join(i)
    for i in anal3:
        print >>g3,' '.join(i)

finally:
    f1.close()
    f2.close()
    f3.close()
    g1.close()
    g2.close()
    g3.close()
