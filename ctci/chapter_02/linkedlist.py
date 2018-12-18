class Node:
	def __init__(self,data):
		self.value = data
		self.next = None

class linkedlist:
	def __init__(self):
		self.head = None

	def push(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	def append(self, data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
			return self.head
		
		cur = prev = self.head
		while(cur):
			prev = cur
			cur = cur.next
		prev.next = newNode


	def insertAfter(self, prev, data):
		cur = self.head
		newNode = Node(data)
		while(cur):
			if cur.value == prev:
				newNode.next = cur.next
				cur.next = newNode
			cur = cur.next

	def printll(self):
		while(self.head):
			print(self.head.value)
			self.head = self.head.next

if __name__ == '__main__':
	ll = linkedlist()
	ll.push(1)
	ll.push(2)
	ll.push(9)
	ll.insertAfter(2,5)
	ll.printll()






