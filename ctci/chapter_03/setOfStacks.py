class SetOfStacks:
	def __init__(self, capacity):
		self.capacity = capacity
		self.stack = []


	def push(self, value):
		if len(self.stack) == 0 or len(self.stack[-1]) == self.capacity:
			self.stack.append([])
		self.stack[-1].append(value)

	def pop(self):
		if not self.stack:
			return None
		else:
			if self.stack[-1]:
				data = self.stack[-1].pop()
			else:
				self.stack.pop()
		return data 

	def popAt(self, index):
		if index < 1 or index > len(self.stack) or len(self.stack[index-1])==0:
			return None
		else:
			return self.stack[index-1].pop()


def test():
    setofstacks = SetOfStacks(8)
    for i in range(24):
        setofstacks.push(i)
        print i,
    print ""

    for i in range(5):
        print "Popped", setofstacks.pop()

    print "Test for popAt"
    for i in range(5):
        for i in range(3):
            print "Popped", setofstacks.popAt(i+1)


if __name__ == "__main__":
    test()