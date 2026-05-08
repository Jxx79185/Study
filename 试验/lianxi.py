class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # 创建哑节点简化操作
        current = dummy      # 当前指针
        carry = 0            # 进位值
        
        # 遍历两个链表直到都结束且进位为0
        while l1 or l2 or carry:
            # 获取当前节点的值（如果节点存在）
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 计算总和和进位
            total = val1 + val2 + carry
            carry = total // 10  # 计算进位
            digit = total % 10   # 计算当前位数字
            
            # 创建新节点并移动指针
            current.next = ListNode(digit)
            current = current.next
            
            # 移动原始链表指针（如果存在）
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next  # 返回结果链表的头节点