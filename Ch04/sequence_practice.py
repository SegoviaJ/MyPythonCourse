nums=[65,987,654,2,18,687,22,36]

lowest=nums[0]
for x in nums:
    if x<lowest:
        lowest=x
print(lowest)