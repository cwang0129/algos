from linkedlist import linkedlist
from linkedlist import Node

def partition(ll, x):
	h1 = l1 = Node(0)
	h2 = l2 = Node(0)

	while(ll.head):
		if(ll.head.value < x):
			l1.next = ll.head
			l1 = l1.next
		else:
			l2.next = ll.head
			l2 = l2.next
		ll.head = ll.head.next
	l1.next = h2.next
	l2.next = None
	return l1.next

