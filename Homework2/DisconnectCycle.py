class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
    
def insertAtFront( head,  val): #creates new Node with data val at front; returns new head
    new_node = Node(val)
    new_node.next = head
    return new_node
def insertAtBack(head, val): #creates new Node with data val at end
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = Node(val)
def insertAfter(head,  val, loc): #creates new Node with data val after Node loc
    curr = head
    count = 0
    while loc != count and curr.next != None:
        curr = curr.next
        count+=1
    saved = curr.next
    new = Node(val)
    curr.next = new
    new.next = saved
def deleteFront(head): #removes first Node; returns new head
    saved = head.next
    head = saved
    return saved

def deleteBack(head): #removes last Node
    curr = head
    if head == None:
        return 0
    while curr.next:
        curr = curr.next
    curr = None

def deleteNode(head, loc): #deletes Node loc; returns head
    curr = head
    while curr.next != loc:
        curr = curr.next
    saved = curr.next.next
    curr.next = saved
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
def reverseIterative( head): #reverses the linked list iteratively
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
    while curr:
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

def disconnect(list):
    list_check = []
    curr = list
    while curr:
        if curr.data not in list_check:
            list_check.append(curr.data)
        if curr.next and curr.next.data not in list_check:
            list_check.append(curr.next.data)
        else:
            curr.next = None
        curr = curr.next
    return list

        
palindrome = Node(1)
palindrome.next = palindrome
debug_print(disconnect(palindrome))