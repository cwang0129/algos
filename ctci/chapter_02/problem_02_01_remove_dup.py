from linkedlist import linkedlist

def remove_dup(unsort_ll):
	if unsort_ll.head is None:
		return

	cur = unsort_ll.head
	while(cur):
		runner = cur
		while(runner.next):
			if cur.value == runner.next.value:
				runner.next = runner.next.next
			else:
				runner = runner.next
		cur = cur.next




ll = linkedlist()
ll.push(2)
ll.push(8)
ll.append(3)
ll.append(8)
ll.push(2)
ll.printll()
remove_dup(ll)
ll.printll()