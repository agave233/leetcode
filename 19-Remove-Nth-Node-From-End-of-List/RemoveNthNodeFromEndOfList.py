class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = p2 = head
        k = 0
        while p2 != None:
            p2 = p2.next
            k += 1
        n = k - n + 1
        if n == 1:
            return p1.next
        for i in range(n - 2):
            p1 = p1.next
        p1.next = p1.next.next
        return head