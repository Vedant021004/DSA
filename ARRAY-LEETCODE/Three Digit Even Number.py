import math

def findnumber(nums):
    count = 0
    for num in nums:
        digit = int(math.log10(num)) + 1

        if digit % 2 ==0:
            count +=1

    return count 

obj = findnumber([12,23,456,7894])        
print(obj)



# if i need for three values 

import math

def find_for_threes(nums):
    count = 0
    for num in nums:
        digit = int(math.log10(num)) + 1
        if digit ==3 and num %2 == 0:
            count +=1

    return count

obj = find_for_threes([1222,222,456,446,98,12])        
print(obj)
