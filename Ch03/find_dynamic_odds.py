counter=0

limit=input('Enter your limit if wanted: ')

if not limit:
    limit='4'

limit=int(limit)

while True:
    if counter==limit:
        break
    if counter%2!=0:
        print(counter, end=" ")
    counter+=1
print('\n''Fin')