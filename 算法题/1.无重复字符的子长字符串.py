# s=input('请输入一串字符串:')
# 'adearswfad'
# li=[]
# li_len=0
# for i in range(len(s)-1):  
#     if len(li)==0:  
#         li.append(s[i])
#     if s[i]!=s[i+1] and s[i+1] not in li: 
#         li.append(s[i+1])  

#         if len(li)>li_len:
#             li_len=len(li)

#     else:
#         li.clear()


# print(li_len)






class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0        # 窗口左边界
        max_len = 0     # 最长子串长度
        char_index = {} # 存储字符最后出现的位置
       
        for right in range(len(s)):
            # 若当前字符已存在且在当前窗口内
      
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1  # 移动左边界到重复字符的下一位
            
            # 更新当前字符的位置
            char_index[s[right]] = right
            
            # 计算当前窗口长度并更新最大值
            cur_len = right - left + 1
            if cur_len > max_len:
                max_len = cur_len
        
        return max_len

a=Solution()
print(a.lengthOfLongestSubstring('adearswfad'))