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

def dedup_sorted_list(list):
    curr = list
    prev = None
    future = curr.next
    while curr:
        if future and curr.data == future.data:
            print("future curr caught = ", curr.data)
            curr.next = curr.next.next
            curr = future
            future = future.next.next

        elif prev and prev.data == curr.data:
            print("prev curr caught = ", curr.data)
            saved_curr = curr
            saved = curr.next
            curr = prev
            curr.next = saved
            if future:
                future = future.next
            curr = curr.next
            prev = saved_curr
            
        else:
            print("curr = ", curr.data)
            prev = curr
            if future:
                future = future.next
            curr = curr.next
        
    return list

carlos = Node(3) 
insertAtBack(carlos, 5)
insertAtBack(carlos, 5)  
insertAtBack(carlos, 7)
insertAtBack(carlos, 7)
insertAtBack(carlos, 8)
insertAtBack(carlos, 10)
debug_print(dedup_sorted_list(carlos))
