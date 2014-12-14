class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getInterSectionNode(self, headA, headB):
        pa = headA
        pb = headB
        numA = 0
        numB = 0
        if pa == None or pb == None:
            return None
        while pa:
            numA = numA + 1
            pa = pa.next
        while pb:
            numB = numB + 1
            pb = pb.next
        if numA > numB:
            i = numA - numB
            while i > 0:
                headA = headA.next
                i = i - 1
        if numB > numA:
            i = numB - numA
            while i > 0:
                headB = headB.next
                i = i - 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
