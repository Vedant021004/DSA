def findNumbers(nums):

    count = 0

    for num in nums:

        if 10 <= num <= 99 or 1000 <= num <= 9999 or num == 100000:
            count += 1

    return count

obj = findNumbers([12,3,4,5678])
print(obj)
