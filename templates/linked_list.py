class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(array):
    node = ListNode()
    current = node
    for val in array:
        current.next = ListNode(val)
        current = current.next
    return node.next

def print_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    vals.append("None")
    print(" -> ".join(vals))

def to_array(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals