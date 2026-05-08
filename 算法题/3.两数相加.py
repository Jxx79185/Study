# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1_v=0
        l2_v=0

        def enumerate_list(self,obj):
            i=0
            while obj:
                yield i,obj.val
                obj=obj.next
                i+=1

                

        for i,j in enumerate_list(l1):
            l1_v+=j*(10**i)

        for i,j in enumerate_list(l2):
            l2_v+=j*(10**i)

        new_v=l1_v+l2_v
        last_v=list(str(new_v))[::-1]
        return last_v
    
l1=[1,3,7]
l2=[3,5,8]
a=Solution()
print(a.addTwoNumbers(l1,l2))