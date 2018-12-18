from linkedlist import linkedlist

def kth_to_last(ll, k):
	cur = ll.head
	cnt = 1

	while(cur):
		if cnt == k:
			print(cur.value)
			k = k+1
		cur = cur.next
		cnt += 1


ll = linkedlist()
ll.push(2)
ll.push(8)
ll.append(3)
ll.append(8)
ll.push(2)
kth_to_last(ll,3)
