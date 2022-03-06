def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    curNode = result = ListNode(0)  # Returning list

    # If l1 is empty no addition will occur return l2
    if l1 == None:
        return l2

    # If l2 is empty no addition will occur return l1
    if l2 == None:
        return l1

    # Store the sum val
    sval = l1.val + l2.val

    # If the sum val does not need a carry
    # instantiate a ListNode with value sumval
    # reference the new node's next to the recursive
    # call of this function passing l1 and l2 next
    if sval < 10:
        ansNode = ListNode(sval)
        ansNode.next = self.addTwoNumbers(l1.next, l2.next)
        return ansNode
    # If the sum val needs a carry, subtract 10 from sum
    # to get right most digit and instantiate new node with said digit
    # set new node.next to recursive call passing carry and l1,l2 nexts
    else:
        rval = l1.val + l2.val - 10
        ansNode = ListNode(rval)
        ansNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
        return ansNode