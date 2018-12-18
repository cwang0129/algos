from linkedlist import linkedlist

def delete_middle_node(ll):
	if ll.head or ll.head.next is None:
		ll.head.value = None
		return ll
	prev = cur = ll.head
	runner = cur
	while(runner.next):
		prev = cur
		cur = cur.next
		runner = runner.next.next
	prev.next = cur.next
	return ll

ll = linkedlist()
ll.push(2)
ll.push(8)
ll.append(3)
ll.append(8)
ll.push(2)
delete_middle_node(ll)
ll.printll()