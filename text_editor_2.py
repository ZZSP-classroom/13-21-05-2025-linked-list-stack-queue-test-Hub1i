# text_editor_2.py
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Example usage
stack = Stack()
stack.push("typed: Hello")
stack.push("deleted: l")

print(stack.pop())  # Should show "deleted: l"
