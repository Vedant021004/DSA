class Solutions:
    def find_max(self,nums):
     count = 0
     max_count = 0

     for i in nums:
         if i == 1:
            count += 1
            max_count = max(max_count,count)
         else :
            count = 0
     return max_count          
            
object = Solutions()
result = object.find_max([1,0,2,0,0,1,1,1,1])
print(result)
