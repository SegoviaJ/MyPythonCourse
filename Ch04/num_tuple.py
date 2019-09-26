some_nums=(2,6,4,2,22,54,12,8,-1)

print(len(some_nums))
print('the sum is:',sum(some_nums))
print(some_nums[3])

highest_num=some_nums[0]
for x in some_nums:
    if x > highest_num:
        highest_num=x
print('Highest is:', highest_num)
print(some_nums)
print()

# for x in range(len(some_nums)):
#     print(x)
#     if (x%2==0):
#         some_nums[x]=11
# print(some_nums)

