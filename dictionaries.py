# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:42:00 2021

@author: Dahire
"""
#DICTIONARIES{}
#they are mutale
#they have key which contains some values

#cerating a dictionary
d1=dict()
d1['fruits']='apple'
d1['name']='john'
d1['number']=10
print(d1)

#mutating a dictionary
d1['number']=d1['number']+5
print(d1)

#checking the key in dictionary
'key' in dict() #returns logical TRUE/FALSE

#counting the wrods in the dictionary or in a para using dictinary
d={}
line=input("Enter the line of text: ")
words=line.split()
#  print(words)
for word in words:
    d[word]=d.get(word,0)+1 #in d.get(word,0) if the key is not there the count is zero
print(d)

#loop for disctoinary
for key in d1:
    print(key,d1[key])

#making the lsit of keys and values
print(d1.keys())
print(d1.values())
print(d1.items())#this will gives tuples

#print dictionary with its key and values using two iteration variable loop
for a,b in d1.items():
    print(a,b)

#GRADED ASSIGNMENT 9.4
#Write a program to read through the mbox-short.txt and figure out who has sent
#the greatest number of mail messages. The program looks for 'From ' lines and
#takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to
#a count of the number of times they appear in the file. After the dictionary is produced,
#the program reads through the dictionary using a maximum loop to find the most prolific
#committer.

fname="mbox-short.txt"
fh=open(fname)
mail=dict()
for line in fh:
    if not line.startswith('From '):
        continue
    l=line.rstrip()
    w=l.split()
    mailid=w[1]
    mail[mailid]=mail.get(mailid,0)+1
#to get the mailid(key) with largest value
largest=None
for k,v in mail.items():
    if largest is None:
        largest=v
    elif largest<v:
        largest=v
        keyword=k
#k=max(mail, key=mail.get) another way to get the largest value anf the key of it
print(keyword,largest)
fh.close()
