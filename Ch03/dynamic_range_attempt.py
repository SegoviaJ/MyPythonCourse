start=input('Start: ')
if not start:
    start='0'
start=int(start)

end=input('End: ')
if not end:
    end='100'
end=int(end)

step=input('Step: ')
if not step:
    step='1'
step=int(step)

loop=True

while loop==True:
    print('Do you wish to include:\n\n1. All numbers\n\n2. Evens\n\n3. Odds\n\n4. Exit\n')
    selection=input('Please make your selection: ')
    if selection=='1':
        for numbers in range(start,end,step):
            print(numbers,end=" ")
    if selection=='2':
        for numbers in range(start,end,step):
            if numbers%2==0:
                print(numbers,end=" ")
    if selection=='3':
        for numbers in range(start,end,step):
            if numbers%2!=0:
                print(numbers,end=" ")
    if selection=='4':
        break
    print('\n')
loop=False

