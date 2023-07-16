class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
        self.prev = None
    
def insertAtFront( head,  val): #creates new Node with data val at front; returns new head
    new_node = Node(val)
    new_node.next = head
    return new_node
def insertAtBack(head, val): #creates new Node with data val at end
    curr = head
    while curr.next:
        curr = curr.next
    saved = curr
    curr.next = Node(val)
    curr.next.prev = saved
def insertAfter(head,  val, loc): #creates new Node with data val after Node loc
    curr = head
    count = 0
    while loc != count and curr.next != None:
        curr = curr.next
        count+=1
    saved = curr.next
    new = Node(val)
    curr.next = new
    curr.next.prev = curr
    new.next = saved
    new.next.prev = curr.next
def deleteFront(head): #removes first Node; returns new head
    saved = head.next
    saved.prev = None
    head = saved
    return saved

def deleteBack(head): #removes last Node
    curr = head
    if head == None:
        return 0
    while curr.next:
        curr = curr.next
    curr.prev.next = None
    curr = None

def deleteNode(head, loc): #deletes Node loc; returns head
    curr = head
    while curr.next != loc:
        curr = curr.next
    saved = curr.next.next
    curr.next = saved
    curr.next.prev = curr
    return head

def length(head): #returns length of the list
    if head == None:
        return 0
    curr = head
    count = 1
    while curr.next:
        count+=1
        curr = curr.next
    return count
def reverseIterative(head): #reverses the linked list iteratively
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head
def debug_print(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
def reverseRecursive(head): #reverses the linked list recursively (Hint: you will need a helper function)
    if (head == None):
        return head
         
    if (head.next == None):
        return head
    node1 = reverseRecursive(head.next)
    head.next.next = head
    head.next = None
    return node1

carlos = Node(3)
insertAtBack(carlos, 5)
insertAtBack(carlos, 6)
insertAtBack(carlos, 7)
insertAtBack(carlos, 8)
debug_print(reverseIterative(reverseIterative(carlos)))
# debug_print(reverseRecursive(carlos))