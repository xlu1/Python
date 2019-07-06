class Node(object):

    def __init__(self, value=None):  # initialize
        self.next = None  # node pointer
        self.value = value  # node value

    def __repr__(self):  # return a printable representation of the object
        return f'Node({self.value})'
    # f-strings are string literals that have an f at the beginning and
    # curly braces containing expressions that will be replaced with their values


def print_all_nodes(root: Node):
    """
    Write a function to print all nodes of linked list
    """
    node = root
    print("\n\nPrinting all nodes...")
    while node:  # while node is not None, print node value
        print(node)
        if node.next:  # while next node is not None, print arrow
            print("->")
        node = node.next  # set the node to be the next node
    pass


def append(root: Node, value):
    """
    Append a new node of value at the end of linked list
    """
    node = root
    # print(type(node))
    # print(node.value)
    print("\n\nAppending a node at the end...")
    if node.value is None:
        node.value = value
        print(f'There is no node in the linked list yet.\nThis will be the first node.')
        print(node)
    else:
        current = node
        while current.next:
            current = current.next
            # print(current.next)
        current.next = Node(value)
    return node
    pass


def get_kth_node(root: Node, k: int):
    """
    Get the Kth Node of linked list,
    i.e. Give list a - b - c - d, k = 3, return Node c
    """
    current = root
    count = 0
    print(f'\n\nGetting node #{k}...')
    while current is not None:
        if k <= 0:
            print(f'Error')
            break
        elif count == k - 1:
            print(current)
        count += 1
        current = current.next
    return current
    pass


def get_last_kth_node(root: Node, k: int):
    """
    Get Kth node counting from the end of the list
    i.e. Given list a - b - c - d - e - f, k = 2, return Node e
    """
    print(f'\n\nGetting node #{k} from last...')
    if k < 0:
        print(f'Error')
    main_pointer = root
    reference_pointer = root
    count = 0
    if root is not None:
        # First loop: Reference pointer moves to kth node from header
        while count < k:
            if reference_pointer is None:
                print(f'k is greater than the number of nodes')
                return
            reference_pointer = reference_pointer.next
            count += 1
    # Second loop: Both pointers move one node forward each time
    # until there is no more node for reference pointer to move
    while reference_pointer is not None:
        main_pointer = main_pointer.next
        reference_pointer = reference_pointer.next
    print(f'Node #{k} from last is {main_pointer}.')
    return
    pass


def get_mid_node(root: Node):
    """
    Get the node at middle position of linked list
    i.e. If the given linked list is 1 -> 2 -> 3 -> 4 -> 5 then the output should be 3
         If the given linked list is 1 -> 2 -> 3 -> 4 -> 5 -> then the output should be 4
    """
    slow_pointer, fast_pointer = root, root
    print(f'\n\nGetting the middle node...')
    if root.value is None:
        print(f'There is no node in the linked list.')
    else:
        while (fast_pointer.next is not None) and (slow_pointer.next is not None):
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        print(f'The middle node is {slow_pointer}.')
    pass


def reverse(root: Node):
    """
    Reverse a linked list
    """
    print(f'\n\nReversing the linked list...')
    if root is None or root.next is None:
        print(root)
        return
    previous_node, current_node, next_node = None, root, root.next
    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    reversed_list = previous_node
    print_all_nodes(reversed_list)
    return
    pass


def has_loop(root: Node):
    """
    Check if a linked list contains loop
    """
    slow_pointer, fast_pointer = root, root
    print(f'\n\nChecking if the linked list contains loop...')
    if root.value is None:
        print(f'There is no node in the linked list.')
    else:
        while (fast_pointer is not None) and \
                (fast_pointer.next is not None) and \
                (slow_pointer.next is not None):
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if slow_pointer == fast_pointer:
                print(f'There is a loop.')
                return
        print(f'There is no loop.')
    pass


def get_loop_node(root: Node):
    """
    Given a linked list which contains loop
    Return the location of starting node of loop
    """
    slow_pointer, fast_pointer = root, root
    print(f'\n\nGetting the location of starting node of loop (if any)')
    if root.value is None:
        print(f'There is no node in the linked list.')
    else:
        while (fast_pointer is not None) and \
                (fast_pointer.next is not None) and \
                (slow_pointer.next is not None):
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if slow_pointer == fast_pointer:
                slow_pointer = slow_pointer.next
                print(f'There is a loop at {slow_pointer}.')
                return
        print(f'There is no loop.')


if __name__ == '__main__':
    f = Node()  # test 1: no node
    a, b, c, d, e = (Node(i) for i in range(1, 6))  # test 2: normal list
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    v, w, x, y, z = (Node(i) for i in range(1, 6))  # test 3: loop test
    v.next = w
    w.next = x
    x.next = y
    y.next = z
    z.next = w
    # print_all_nodes(f)
    # print_all_nodes(a)
    # append(f, 4)
    # append(a, 4)
    # get_kth_node(a, 3)
    # get_kth_node(f,1)
    # get_last_kth_node(a, 3)
    # get_last_kth_node(f, 1)
    # get_mid_node(a)
    # get_mid_node(f)
    # reverse(a)
    # reverse(f)
    # has_loop(v)
    # has_loop(a)
    # has_loop(f)
    # get_loop_node(v)
    # get_loop_node(a)
    # get_loop_node(f)
