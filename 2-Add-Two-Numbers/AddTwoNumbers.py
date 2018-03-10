class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add = l1.val + l2.val
        out = ListNode(add % 10)
        head = out
        
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            plus = (add > 9 and 1 or 0)
            add = l1.val + l2.val + plus
            one = ListNode(add % 10)
            out.next = one
            out = out.next
            
        plus = (add > 9 and 1 or 0)
        l = l1.next and l1.next or l2.next
        
        if plus == 0:
            out.next = l
        else:
            if l:
                l.val = l.val + 1
                lp = l
                while lp.val == 10:
                    lp.val = 0;
                    if lp.next != None:
                        lp = lp.next
                        lp.val = lp.val + 1
                    else:
                        lp.next = ListNode(1)
                        break
                out.next = l
            else:
                out.next = ListNode(1)
        return head