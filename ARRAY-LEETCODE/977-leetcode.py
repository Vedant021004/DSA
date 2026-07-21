# target = square of the sorted array 
# eg. [0,1,9,16,100]

arr = [0,-1,-4,10,5]

for i in range(len(arr)):
    arr[i] = arr[i] * arr[i]


new = []

while arr:

    maximum = arr[0]

    for num in arr:

        if num > maximum:

            maximum = num

    new.insert(0, maximum)

    arr.remove(maximum)

print(new)


# my approach

arr = [3,2,4,5,6,3]
max = []

for i in arr:
    squ = i*i
    max.append(squ)

max.sort() 
print(max)   


class Solution(object):
    def sortedSquares(self, nums):
        max = []
        for i in nums:
            square = i*i
            max.append(square)
        max.sort()

        return max
obj = Solution()
answer = obj.sortedSquares([-4,-1,0,3,10])
print(answer)