class minStack:
	def __init__(self):
		self.stack = []
		self.min = []

	def push(self, value):
		self.stack.append(value)
		if len(self.min) == 0 or value < self.min[-1]:
			self.min.append(value)

	def pop(self):
		val = self.stack.pop()
		if val == self.min[-1]:
			self.min.pop()

	def get_min(self):
		if len(self.min) == 0:
			return None
		else:
			return self.min[-1]


if __name__ == '__main__':
	s1 = minStack()
	s1.push(3)
	s1.push(2)
	print(s1.get_min())  # return 2
	s1.push(1)       
	print(s1.get_min()) # return 1
	s1.pop()
	print(s1.get_min()) # return 2

