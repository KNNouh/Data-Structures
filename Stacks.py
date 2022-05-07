class Node:
    def __init__(self):
        self.nextNode = None
        self.content = ""

class Stack:

    def __init__(self, item):
        self.base = Node()
        self.base.content = item

    def push(self, content):
        oldBase = self.base
        self.base = Node()
        self.base.content = content
        self.base.nextNode = oldBase

    def pop(self):
        if not self.base:
            return "It Is Empty"
        wantedValue = self.base.content
        self.base = self.base.nextNode
        return wantedValue

    def is_empty(self):
        return not self.base


MyStack = Stack("Karim")
MyStack.push('Nabil')
MyStack.push("Atiaa")
MyStack.push("Nouh")
print(MyStack.pop())
print(MyStack.pop())
print(MyStack.pop())
print(MyStack.pop())
print(MyStack.pop())
