import unittest
from text_editor_2 import Stack

class TestTextEditorStack(unittest.TestCase):

    def test_push_pop(self):
        stack = Stack()
        stack.push("typed: Hello")
        stack.push("typed: World")
        
        self.assertEqual(stack.pop(), "typed: World")
        self.assertEqual(stack.pop(), "typed: Hello")
        
    def test_peek(self):
        stack = Stack()
        stack.push("typed: Hello")
        self.assertEqual(stack.peek(), "typed: Hello")

if __name__ == '__main__':
    unittest.main()
