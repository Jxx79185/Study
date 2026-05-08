
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """  
        num=nums2+nums1
        num.sort()
        n=len(num)
        i=n//2
        if n%2!=0:
            num_mid=num[i]
            
        if n%2==0:
            num_mid=(num[i-1]+num[i])/2.0
           
        return num_mid
    


a=Solution()
nums1=[1,2]
nums2=[3,4]
print(a.findMedianSortedArrays(nums1,nums2))