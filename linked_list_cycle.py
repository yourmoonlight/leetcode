class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def has_cycle(self, head):
        fast = slow = head
        if head is None or head.next is None:
            return False
        # judge the fast.next is for the fast = fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
