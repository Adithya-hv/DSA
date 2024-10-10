# Given a singly linked list of numbers. Starting from the head, consider each
# consecutive elements as a group. The leftovers (must be less than ) are considered as a group.
# Please design an algorithm to reverse all elements in each group. Your algorithm should be as
# efficient as possible in both time and space. And, please analyze the time complexity and space
# complexity.

# Node definition for the linked List
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

# Makes a linked list with a given list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Prints a given Linked List
def print_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.value))
        current = current.next
    print(" -> ".join(result))

# Reverses a Group of k elements in list and returns @prev which is the head of the reversed List
# and @curr which is the next element after the group
def reverseGroupInList(head, k):
    prev = None
    curr = head
    i = 0
    
    while curr and i < k:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        i += 1
    return prev, curr

# Main function that returns the result
def reverseInGroups(head, k):
    if not head or k == 1:
        return head
    
    # dummy makes getting the answer easier
    dummy = Node(0)
    dummy.next = head
    # This is where each reversed head is linked to
    groupHead = dummy
    # curr is the current head being operated on
    curr = head
    
    while curr:
        # i keeps track of the number of nodes
        i = 0
        temp = curr
        
        # checks how many nodes are there
        while temp and i < k:
            temp = temp.next
            i += 1

        # reverseGroupInList is called with however many nodes are left 
        if i == k:
            revHead, nextHead = reverseGroupInList(curr, k) 
        else:
            revHead, nextHead = reverseGroupInList(curr, i)
        
        # The group head is connected to the revesed list
        groupHead.next = revHead
        # The node after curr is set to the node after the group completed
        curr.next = nextHead
        # groupHead is reset to curr
        groupHead = curr
        # curr is moved to the node after the reversed group head
        curr = nextHead
    
    # Returns the Head of the result
    return dummy.next
    

if __name__ == "__main__":
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    k = 3
    print("Initial List:")
    print_list(head)
    result = reverseInGroups(head, k)
    

    print(f"Group size: {k}\n")
    print("Result List:")
    print_list(result)