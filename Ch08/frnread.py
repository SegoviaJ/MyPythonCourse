frnlst=[]
with open('friends.txt') as friends:
    while True:
        name=friends.readline().rstrip()
        if not name:
            break
        if name.startswith('#'):
            continue
        else:
            frnlst.append(name)
print(frnlst)
