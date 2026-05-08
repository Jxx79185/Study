

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n=len(s)
        if s < 2:      
            return n
        
        max_len=1
        begin=1

        dp=[[False]*n for _ in range(n)]
        



        


        


s='dwafab11badefaww'
a=Solution()
print(a.longestPalindrome(s))