#program to give grades
score=float(input("Enter score: "))
#print(score)
if score>=0.9 and score<=1.0:
    print('A')
elif score>=0.8 and score<=0.9:
    print('B')
elif score>=0.7 and score<=0.8:
    print('C')
elif score>=0.6 and score<=0.7:
    print('D')
elif score>=0.0 and score<0.6:
    print('F')
else: print('ERROR!!: Score must be between 0.0 and 1.0')


#Createing a function to calculate GROSS PAY for TAXI
def computepay(h,r):
    if h<=40:
        Pay=h*r
        return Pay
    elif h>40:
        Pay=(40*r)+((h-40)*r*1.5)
        return Pay

h= float(input("Enter Hours: "))
r= float(input("Enter Rate: "))
p = computepay(h,r)
print("Pay", p)

# write a program which repeatedly reads number until the user
# enters "done". Once "done" is entered, print outh the total, count,
# and average of the numbers. If the user enters anything other than
# a number, detect their mistake using try and except and print an error
# message and skip to the next number.
num=0
tot=0.0
while True:
    sval=input("Enter a number: ")
    if sval=='done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num=num+1
    tot=tot+fval
    
print(tot,num,tot/num)


# Write a program that repeatedly prompts a user for integer numbers until the
# user enters 'done'. Once 'done' is entered, print out the largest and smallest
# of the numbers. If the user enters anything other than a valid number catch it
# with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.
largest=None
smallest=None
while True:
    number=input('Enter the number: ')
    if number=='done':
        break
    try:
        number=float(number)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest=number
    elif largest<number:
        largest=number
        
    if smallest is None:
        smallest=number
    elif smallest>number:
        smallest=number
    
print('Maximum is',int(largest))
print('Minimum is',int(smallest))


#counnt the numbers of letter a in a string
word='Himanshu Dahire'
b=len(word)#lets the length of the string
count=0
for x in word:
    if x=='h': count=count+1
    
print(count)

#Write code using find() and string slicing to extract the number at the end of
#the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
    #sol1
n=text.find('0')
x=text[n:]
print(float(x))
    #sol2
a=text.find(' ')
b=text.find('5')
y=text[a:b+1]
print(float(y))


#basic code to read a file and convert all chatacters to uppercase
fname = input("Enter file name: ") #takes a name of the file with extension
fh = open(fname) #creats a file handler
for line in fh:
    a=line.upper()
    print(a.rstrip())
fh.close() #this line closes the file

#program to find a string and extract some values
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("the file cannot be opened",fname)
    quit() #quits the after this

fnum=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    sp=line.find(' ')
    num=line[sp:].rstrip()
    count=count+1
    fnum=float(num)+fnum
avg=fnum/count
print("Average spam confidence: ",avg)
