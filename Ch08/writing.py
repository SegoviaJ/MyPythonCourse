family=['Dad','Nikki','James','Trogdor']
handle=open("family.txt","w")

for x in family:
    handle.write(x+'\n')
handle.close()

