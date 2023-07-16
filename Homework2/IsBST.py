class BinarySearchTree:
    def __init__(self, data):
        self.data = data  
        self.right = None  
        self.left = None
         
    def min(self): #returns the minimum value in the BST
        while self.left:
            smaller = self.left
            self = smaller
        return smaller.data
    def max(self): #returns the maximum value in the BST
        while self.right:
            bigger = self.right
            self = bigger
        return bigger.data
    def contains(self, val): #returns a boolean indicating whether val is present in the BST
        ref_left = self
        while ref_left:
            if ref_left.data == val:
                return True
            if ref_left.right != None and ref_left.right.data == val:
                return True
            if ref_left.left != None and ref_left.left.data == val:
                return True
            ref_left = ref_left.left

        ref_right = self
        while ref_right:
            if ref_right.data == val:
                return True
            if ref_right.right!= None and ref_right.right.data == val:
                return True
            if ref_right.left != None and ref_right.left.data == val:
                return True
            ref_right = ref_right.right
        return False
    # For simplicity, do not allow duplicates. If val is already present, insert is a no-op
    def insert(self, val): #creates a new Node with data val in the appropriate location
        if not self.contains(val):
            curr = self
            while curr:
                if val > curr.data:
                    if curr.right == None:
                        curr.right = BinarySearchTree(val)
                        break
                    else:
                        curr = curr.right
                else:
                    if curr.left == None:
                        curr.left = BinarySearchTree(val)
                        break
                    else:
                        curr = curr.left

        else:
            print("Element already present.")
    def print_bst(self):
        curr = self
        while curr:
            if curr.left == None:
                print("left of ", curr.data, " is ", curr.left)
            
            else:
                print("left of ", curr.data, " is ", curr.left.data)

            print("current value ", curr.data)

            if curr.right == None:
                print("right of ", curr.data, " is ", curr.right)
            else:
                print("right of ", curr.data, " is ", curr.right.data)
            curr = curr.left
        
        while curr:
            print("left of ", curr.data, " is ", curr.left.data)
            print("current value ", curr.data)
            print("right of ", curr.data, " is ", curr.right.data)
            curr = curr.right

    def delete(self, val): #deletes the Node with data val, if it exists
        if self.contains(val):
            curr = self
            right_bool = False
            left_bool = False
            while curr:
                if val > curr.data:
                    if curr.right == val:
                        right_bool = True
                        break
                    else:
                        curr = curr.right
                else:
                    if curr.left == val:
                        left_bool = True
                        break
                    else:
                        curr = curr.left
            if right_bool == True:
                delete_this = curr
                from_here = curr.right
                if not from_here.right and not from_here.left:
                    curr.right = None
                if from_here.right and not from_here.left:
                    curr.left = from_here.right
                if from_here.left and not from_here.right:
                    curr.left = from_here.left
                if from_here.left and from_here.right:
                    curr.left = from_here.right
                    curr.left.left = from_here.left
                    if from_here.right.left and not curr.left.left.right:
                        curr.left.left.right = from_here.right.left
            else:
                delete_this = curr
                from_here = curr.left
                if not from_here.right and not from_here.left:
                    curr.left = None
                if from_here.right and not from_here.left:
                    curr.right = from_here.right
                if from_here.left and not from_here.right:
                    curr.right = from_here.left
                if from_here.left and from_here.right:
                    curr.right = from_here.right
                    curr.right.left = from_here.left
                    if from_here.right.left and not curr.right.left.right:
                        curr.right.left.right = from_here.right.left

        else:
            print("Element not in tree! Try again with an actual element of the tree.")
        
def isBST(tree):
    curr_left = tree.left
    curr_right = tree.right
    if curr_left:
        if not (curr_left < tree.data):
            return False
    if curr_right:
        if not (curr_right > tree.data):
            return False

    while curr_left:
        if curr_left.right:
            if not (curr_left.right > curr_left.data):
                return False
        if curr_left.left:
            if not (curr_left.left < curr_left.data):
                return False
        
        curr_left = curr_left.left
    
    while curr_right:
        if curr_right.right:
            if not (curr_right.right > curr_right.data):
                return False
        if curr_right.left:
            if not (curr_right.left < curr_right.data):
                return False
        
        curr_right = curr_right.right
    
    return True

