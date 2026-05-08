
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):          
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j] 
                
        return[]
                







class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable={}
        for i,num in enumerate(nums):
            if target-num in hashtable:
                return [i,hashtable[target-num]]
            
            hashtable[nums[i]]=i


a=Solution()
b=[1,3,5,7,9]
c=10
print(a.twoSum(b,c))
