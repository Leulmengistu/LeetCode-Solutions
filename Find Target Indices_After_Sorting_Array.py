class Solution:
    def targetIndices(self, nums, target: int) :
      
        output = list()
        if target not in nums:
            return output
        else:
            nums = sorted(nums)
            start = nums.index(target)
            while(nums[start]==target):
                output.append(start)
                start+=1
                if(start == len(nums)):
                    break
            return output

c = Solution()
num = [1,2,5,2,3]
print(c.targetIndices(num,5))