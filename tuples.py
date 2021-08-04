# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:08:18 2021

@author: Dahire
"""
#TUPLES()
#it is a kind of sequence that functions like a list.
#They are indexed as ()
#they are "IMMUTABLE"
lettertu=('A','B','C')
numbertu=(1,2,67)

print(numbertu[0])
numbertu[0]=3#IMMUTABLE hence ERROR!!

#assigning values to multiple tuple
(a,b)=(2,'x')
print(a,b)

#sorting dictionary usig tuples
d={"a":10,"d":2,"b":1.6}
x=d.items()#creates a list of tuples containing keys and values
print(x)
print(sorted(x))#sorts based on key values

#if we want to sort based on values then convert value to key
#using
dtemp=list()
for k,v in d.items():
    dtemp.append((v,k))
print(dtemp)
dtemp=sorted(dtemp, reverse=True)#sorts in reverse order
print(dtemp)

#sometnig new 
xx=0
y=[1,2,3,4,5,6,7,8,9,0,10]
for x in y[1:10]:#in Y form index 1 to upto 10 
    xx=xx+1

#list comprehension 
sorted([(v,k) for k,v in d.items()])#VVIMP

#GRADED ASSIGNMENT 10.2
#Write a program to read through the mbox-short.txt and figure out the distribution
#by hour of the day for each of the messages. You can pull the hour out from the 'From '
#line by finding the time and then splitting the string a second time using a colon.
#"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour.
fname='mbox-short.txt'
fh=open(fname)
dhr=dict()
ls=list()
for line in fh:
    if not line.startswith('From '):
        continue
    l=line.rstrip()
    piece=l.split()
    time=piece[len(piece)-2]
    t=time.split(':')
    h=(t[0])
    dhr[h]=dhr.get(h,0)+1
#print(dhr)
#s=sorted([(k,v) for k,v in dhr.items()])
#print(s)
for k,v in dhr.items():
    ls.append((k,v))
ls=sorted(ls)
#print(ls)

for hrs,c in ls:
    print(hrs,c)
fh.close()
