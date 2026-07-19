# Approach 1
# convert the digit into str and then calculate the length  

def find_the_even(nums):
    count = 0

    for num in nums:
        if len(str(num))%2 == 0:
            count +=1

    return count    

obj = find_the_even([12,34,1,2,45322])

print(obj)


# Approach 2
#same but easy
def findNumbers(nums):
    return sum(len(str(num)) % 2 == 0 for num in nums)
obj = findNumbers([12,3,4,56781])
print(obj)

