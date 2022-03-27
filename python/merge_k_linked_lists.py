from typing import List


class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"


def merge_k_linked_lists_brute_force(linked_lists: List[Link]):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_k_linked_lists_brute_force([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists_brute_force([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''
    # Brute force solution
    # Dump all values of all linked lists into a list
    # Sort the list and reconstruct the result linked list
    values = []
    for link in linked_lists:
        while link:
            values.append(link.val)
            link = link.next

    values.sort()

    result = Link(0)
    pointer = result
    for val in values:
        pointer.next = Link(val)
        pointer = pointer.next

    return result.next


def merge_k_linked_lists_suboptimal_solution(linked_lists: List[Link]):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_k_linked_lists_suboptimal_solution([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists_suboptimal_solution([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''
    # Suboptimal solution
    # Look at the front value of all linked lists
    # Find the minimum value and put it in the result linked list
    # "Remove" the value we've added
    # Continue doing until there are no more value to add
    result = Link(0)
    pointer = result

    copied_linked_lists = linked_lists[:]
    while any(copied_linked_lists):
        front_values = [link.val for link in copied_linked_lists if link]
        min_value = min(front_values)

        for i, link in enumerate(copied_linked_lists):
            if link and link.val == min_value:
                pointer.next = Link(link.val)
                pointer = pointer.next
                copied_linked_lists[i] = link.next

    return(result.next)


def merge_k_linked_lists_priority_queue_solution(linked_lists: List[Link]):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_k_linked_lists_priority_queue_solution([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists_priority_queue_solution([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''
    # An improvement of suboptimal solution
    # Look at the front value of all linked lists
    # Find the minimum value and put it in the result linked list
    # "Remove" the value we've added
    # Continue doing until there are no more value to add
    from collections import defaultdict
    from queue import PriorityQueue

    result = Link(0)
    pointer = result

    val_to_link = defaultdict(list)
    pq = PriorityQueue()
    for link in linked_lists:
        val_to_link[link.val].append(link)
        pq.put(link.val)

    while len(val_to_link):
        min_value = pq.get()  # O(log n)
        link = val_to_link[min_value].pop()
        pointer.next = link
        pointer = pointer.next

        if not len(val_to_link[min_value]):
            val_to_link.pop(min_value)
        if link.next:
            val_to_link[link.next.val].append(link.next)
            pq.put(link.next.val)

    return(result.next)
