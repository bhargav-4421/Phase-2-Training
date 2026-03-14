class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0,head)
        cur=dummy
        dif=dummy
        for i in range(n):
            dif=dif.next
        while dif.next:
            cur=cur.next
            dif=dif.next
        cur.next=cur.next.next
        return dummy.next
