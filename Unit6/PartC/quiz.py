class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        # Traverse both lists
        while pA != pB:
            # If we reach the end of one list, start at the beginning of the other
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA