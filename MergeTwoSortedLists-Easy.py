class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoListsIterativley(self, l1, l2):
    dummy = cur = ListNode(0)

    # While both lists are not None
    while l1 and l2:
        # if the list1 value is smaller than list2 value
        # set the next reference in our ListNode to list1
        # update l1 to traverse list
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        # otherwise set next reference in our ListNode to list2
        # update l2 to traverse
        else:
            cur.next = l2
            l2 = l2.next
        # update cur to traverse
        cur = cur.next
    # set cur next reference to remaining hanging digits,
    # i.e l1 = [1,2,3] l2 = [1,2,3,4,5] -> l2's [4,5]
    cur.next = l1 or l2
    return dummy.next

def mergeTwoListsRecursivley(self, l1, l2):
    # if either list is empty return the non empty one
    if not l1 or l2:
        return l1 or l2
    # if list1 value is smaller call function again with
    # next l1 and same l2, update l1 reference, repeats until
    # l1 is sorted with all l2 values, return l1
    if l1.val < l2.val:
        l1.next = self.mergeTwoListsRecursivley(l1.next, l2)
        return l1
    # same as above but updates and returns l2
    else:
        l2.next = self.mergeTwoListsRecursivley(l1, l2.next)
        return l2

def mergeTwoListsInPlace(self, l1, l2):
    if not (l1 and l2):
        return l1 or l2
    if l2.val < l1.val:
        l1, l2 =  l2, l1
    res = l1
    while l1.next and l2:
        if l2.val < l1.next.val:
            temp = l1.next
            l1.next = l2
            l2 = l2.next
            l1.next.next = temp
        l1 = l1.next
    if l2:
        l1.next = l2
    return res














