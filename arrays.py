import random
from random import randint
d = dict()
input_n = input("Введите N: ")
n = int(input_n)
l = list(range(1, n*5))
random.shuffle(l)
for i in range(n):
    d['num_%s' % i] = [0]*l[i]
for i in range(n):
    for j in range(len(d['num_%s' % i])):    
        d['num_%s' % i][j] = randint(1, 99999)
for i in range(n):
    print("Размер массива num",i,"=",len(d['num_%s' % i]))
    for j in range(len(d['num_%s' % i])):    
        d['num_%s' % i].sort()
        if i%2 == 0:
            d['num_%s' % i].reverse()
        print(j,":",d['num_%s' % i][j])