class Node:
    """Class that implements a Node"""
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    """Class for LinkedList"""
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def not_present(llist, item):
    if llist.head is None:
        return True
    current_node = llist.head
    while current_node:
        if current_node.value == item:
            return False
        current_node = current_node.next
    return True

def union(llist_1, llist_2):
    if llist_1.head is None:
        return llist_2
    if llist_2.head is None:
        return llist_1
    # Your Solution Here
    current_node = llist_1.head
    new_ll = LinkedList()
    def run_through_ll(current_node,new_ll):
        while current_node:
            if not_present(new_ll, current_node.value):
                new_ll.append(current_node.value)
            current_node = current_node.next

    run_through_ll(current_node,new_ll)
    current_node = llist_2.head
    run_through_ll(current_node, new_ll)
    return new_ll



def intersection(llist_1, llist_2):
    # Your Solution Here
    new_ll = LinkedList()
    cache = []
    current_node = llist_1.head
    while current_node:
        current_node2 = llist_2.head
        while current_node2:
            if current_node.value == current_node2.value:
                new_ll.append(current_node.value)
            current_node2 = current_node2.next
        current_node = current_node.next
    if new_ll.head is None:
        return "No intersection"
    return new_ll


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('union')
print (union(linked_list_1,linked_list_2))
print('intersection')
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print('union')
print (union(linked_list_3,linked_list_4))
print('intersection')
print (intersection(linked_list_3,linked_list_4))