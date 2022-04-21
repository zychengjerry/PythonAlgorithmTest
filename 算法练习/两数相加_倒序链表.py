class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_Loop:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        re = result
        carry = 0
        # l1,l2,进位 有一个存在则需要继续链表
        while l1 or l2 or carry > 0:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            re.next = ListNode((x + y + carry) % 10)
            re = re.next
            # 进位
            carry = (x + y + carry) // 10
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return result.next

class Solution_Recursion:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 某一个加数不存在，那么结果即为另一个加数
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # 加数都存在，取对位相加，除以10取余
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        re = ListNode((x + y) % 10)

        # 下一个节点，即为l1和l2下一个节点相加，再加上此节点的进位
        re.next = self.addTwoNumbers(l1.next, l2.next)
        if x + y > 9:
            re.next = self.addTwoNumbers(re.next, ListNode((x + y) // 10))

        return re