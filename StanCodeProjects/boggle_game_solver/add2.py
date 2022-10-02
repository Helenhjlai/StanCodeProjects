"""
File: add2.py
Name: Helen Lai
------------------------
There are two linked lists represent two positive number respectively.
However, the value of each linked list is stored reversely, that means the value of a linked list 1-->2-->3
is '321'.
This program will calculate the two value of two given linked lists and return a new linked list of that value.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    # find l1 elements
    lst1 = find_l(l1)
    # reverse l1
    lst1_rev = lst_rev(lst1)

    lst2 = find_l(l2)
    lst2_rev = lst_rev(lst2)

    add_num = str(lst1_rev + lst2_rev)

    # add2 linked list
    add_queue = None
    for i in range(len(add_num) - 1, -1, -1):
        new_add_node = ListNode(int(add_num[i]), None)
        if add_queue is None:
            add_queue = new_add_node
        else:
            # append
            cur = add_queue
            while cur.next is not None:
                cur = cur.next
            cur.next = new_add_node
    #######################
    return add_queue


def lst_rev(lst):
    """
    :param lst: lst, lst of a linked list for reversed
    :return: int, a number represents the right value
    """
    lt_rev = ''
    for i in range(len(lst)):
        ele = lst.pop()
        lt_rev += str(ele)
    return int(lt_rev)


def find_l(linked_list):
    """
    :param linked_list: ListNode, a linked list to find all elements in
    :return: lst, a list stores the value of the given linked list.
    """
    lst = []
    cur = linked_list
    if cur.next is None:
        lst.append(cur.val)
    else:
        while cur is not None:
            lst.append(cur.val)
            cur = cur.next
    return lst

####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
