print("1.Read content of file")
print("2.Read first to specific line of file")
print("3.Read line by line and store in a list")
print("4.Find longest word in file")
print("5.Count the number of lines in file")
print("6.count the frequnecy of a word")
print("7.Read the random line in a file")

ch=int(input("enter your choice:"))
file="1_datatypes.py"

if ch==1:
    print("Content of file are:")
    txt=open(file).read()
    print(txt)

if ch==2:
    line=int(input("enter the number of line:"))
    from itertools import islice
    with open(file) as txt:   
        for i in islice(txt,line):
            print(i)

if ch==3:
    print("Reading line by line and storing in list:")
    with open(file)as txt:
        list=txt.readlines()
    print(list) 

if ch==4:
    print("Longest word is:")
    word=open(file).read().split()
    longest_word='a'
    for i in word:
        if len(i)>=len(longest_word):
            longest_word=i
    print(longest_word)

if ch==5:
    line=open(file).read().splitlines()
    print(len(line))

if ch==6:
    from collections import Counter
    with open(file) as txt:
        print(Counter(txt.read().split()))

if ch==7:
    import random
    print("random line is:")
    line=open(file).read().splitlines()
    print(random.choice(line))




