def sortList(self, head: ListNode) -> ListNode:
    L = []

    while head:
        L.append(head.val)
        head = head.next

    L.sort()

    dummy = cur = ListNode(0)

    for e in L:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next