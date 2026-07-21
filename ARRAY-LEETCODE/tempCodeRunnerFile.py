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