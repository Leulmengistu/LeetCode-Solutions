class Solution:
    def containsDuplicate(self, nums) -> bool:
        value = False
        num = sorted(nums)
        
        for i in range(len(num)):
            if(i==len(num)-1):
                return False
            else:
                if(num[i] == num[i+1]):
                    return True
        
        return False        
    
class Solutions:
    def containsDuplicate(self, nums) -> bool:
        if len(nums)!= len(set(nums)):
            return True
        return False