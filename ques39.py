class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # next node store
        curr.next = prev        # link reverse
        prev = curr             # prev move
        curr = next_node        # curr move

    return prev