import sys
number=int(sys.argv[1])
word=sys.argv[2:10]

for x in word:
    if len(x)>number:
        print(x)
