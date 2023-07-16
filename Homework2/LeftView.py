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

def leftview(tree, dict_levels, count):
    if tree:

        # First recur on left child
        leftview(tree.left, dict_levels, count+1)

        # Then print the data of node
        if count in dict_levels:
           dict_levels[count].append(tree.data)
        else:
           dict_levels[count] = [tree.data]

        # Now recur on right child
        count = 0
        leftview(tree.right, dict_levels, count+1)
    
    final_min = []
    print(dict_levels)
    for i in dict_levels:
        final_min.append(min(dict_levels[i]))
    return final_min


carlos = BinarySearchTree(10)
carlos.right = BinarySearchTree(12)
carlos.left = BinarySearchTree(4)
carlos.right.right = BinarySearchTree(24)
carlos.left.left = BinarySearchTree(2)
carlos.left.left.right = BinarySearchTree(3)
carlos.print_bst()
print(leftview(carlos, {}, 0))


#  10
# 4  12
#2     24
# 3