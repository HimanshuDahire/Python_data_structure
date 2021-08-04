# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 14:25:54 2021

@author: Dahire
"""
#LISTS[]
#lists are surrounded by square brackates and oblects are separated by commas
#creating a list
var=['A','C','z',10,2.5,['ab','xy'],'name']
fruits=['apple','banana','guava']
cities=['raigarh','raipur','bilaspur']

#list indexing
var[3]
print(var[3:6])#including 3 upto 6 but not including 6

#range function in the list
print(range(var)) #range only works for integer variables like below
x=print(range(len(var)))

for y in range(len(fruits)): #using range for counted loop
    print("at index",y,"in list fruit, exists",fruits[y])

for city in cities: #looping using list
    print("I lived in",city)

#concatanation of the lists
newls=fruits+cities #adds two lists subtrsction doesnot works here
print(newls)

#mutating the  list as they are muatble
newls[4]='Bhilai'
print(newls)

#using append to add some data to list
ls=[] #an enpety list
ls.append('abc')
ls.append(99,200,2.33)#append takes exactly one agruement hence error
ls.append(2.33) #this is correct

#checking something is in the list or not
'A' in var #returns true or false
'apple' in var
'apple' not in var

#sort in the list
fruits.sort()
cities.sort()
print(cities)

#other operations in the list
numls=[1,3,5,23,90,100,2.2,4.6,9.9,23]
print(max(numls))
print(min(numls))
print(sum(numls))
print(len(numls))

print(max(fruits))
print(min(fruits))

#splitting the string and creating the list
st="write three words"
stls=st.split()#splits the string from spaces
print(stls)

st="write;three;words"
stls=st.split(';')#splits the string from ";"
print(stls)

#GRADED ASSIGNMENT 8.4
#QUESTION: Open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.
fname = input("Enter file name: ")
fh = open(fname)
ls=[] #or we can also write ls=list()
for line in fh:
    l=line.rstrip()
    words=l.split()
    for word in words:
        if word not in ls:
            ls.append(word)
ls.sort()
print(ls)
fh.close()

#GRADED ASSIGNMENT 8.5
#Open the file mbox-short.txt and read it line by line.
#When you find a line that starts with 'From ' like the following line:
#"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
#You will parse the From line using split() and print out the second word in the line
#Then print out a count at the end.
fname="mbox-short.txt"
fh=open(fname)
count=0
for line in fh:
    if not line.startswith('From '):
        continue
    #print(line)
    l=line.rstrip()
    words=l.split()
    print(words[1])
    count=count+1
print("There were", count, "lines in the file with From as the first word")
fh.close()