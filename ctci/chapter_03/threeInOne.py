class MultiStack:

	def __init__(self, numStack, sizeStack):
		self.numStack = numStack
		self.sizeStack = sizeStack
		self.stack = [0] * numStack * sizeStack
		self.pointer = [-1] * numStack

	def push(self, numStack, value):
		if self.isFull(numStack):
			print('current stack is full')
		else:
			self.pointer[numStack] += 1
			index = self.indexOfTop(numStack)
			self.stack[index] = value

	def pop(self, numStack):
		if self.isEmpty(numStack):
			return ('current stack is empty')

		else:
			index = self.indexOfTop(numStack)
			result = self.stack[index]
			self.pointer[numStack] -= 1
			return result

	def peek(self, numStack):
		if self.isEmpty(numStack):
			print('current stack is empty')
		else:
			index = self.indexOfTop(numStack)
			return self.stack[index]

	def isEmpty(self, numStack):
		return self.indexOfTop(numStack) == -1

	def isFull(self, numStack):
		return self.pointer[numStack] + 1 >= self.sizeStack

	def indexOfTop(self, numStack):
		return numStack * self.sizeStack + self.pointer[numStack]


if __name__ == '__main__':
    array = MultiStack(3, 2)
    array.push(2, 11)
    array.push(2, 13)
    print(array.pop(0))  # Trying to pop an empty stack.
    print(array.peek(2))# 13
    array.push(0, 20)
    array.push(0, 30)
    print(array.pop(0))  # 30
    print(array.peek(0)) # 20

