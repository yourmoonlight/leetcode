# given a linked list, remove the nth node from the end of list.
# definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        p = ListNode(1)
        p.next = head
        p1 = p
        p2 = p
        for i in range(n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return p.next
