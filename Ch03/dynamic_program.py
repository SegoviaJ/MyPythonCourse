good=False

while not good:
    start=int(input('Start: '))
    end=int(input('End: '))
    step=int(input('Step: '))
    
    if start<end and step>0:
        good=True
    elif start>end and step<0:
        good=True

good=False
while not good:
    print('Do you wish to include:\n\n1. All numbers\n\n2. Evens\n\n3. Odds\n')
    selection=input('Please make your selection: ')
    if selection=='1' or selection=='2' or selection=='3':
        good=True

if selection=='1':
    for numbers in range(start,end,step):
        print(numbers,end=" ")
elif selection=='2':
    for numbers in range(start,end,step):
        if numbers%2==0:
            print(numbers,end=" ")
elif selection=='3':
    for numbers in range(start,end,step):
        if numbers%2!=0:
            print(numbers,end=" ")
print('\n')

