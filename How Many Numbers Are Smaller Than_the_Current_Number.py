class Solution:
    def smallerNumbersThanCurrent(self, nums):
        
        sortedList = sorted(nums)
        outputList = list()
        for item in nums:
            index = sortedList.index(item,0)
            outputList.append(index)

        return outputList
       