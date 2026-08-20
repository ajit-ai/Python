from algorithms.stack.stack import ArrayStack, LinkedListStack
from algorithms.stack.valid_parenthesis import is_valid


class TestArrayStack:
    def test_push_pop(self):
        s = ArrayStack()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        assert s.pop() == 1

    def test_peek(self):
        s = ArrayStack()
        s.push(10)
        assert s.peek() == 10
        assert len(s) == 1

    def test_is_empty(self):
        s = ArrayStack()
        assert s.is_empty() is True
        s.push(1)
        assert s.is_empty() is False

    def test_len(self):
        s = ArrayStack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert len(s) == 3

    def test_pop_empty(self):
        import pytest
        s = ArrayStack()
        with pytest.raises(IndexError):
            s.pop()

    def test_peek_empty(self):
        import pytest
        s = ArrayStack()
        with pytest.raises(IndexError):
            s.peek()

    def test_expand(self):
        s = ArrayStack(size=2)
        for i in range(10):
            s.push(i)
        assert len(s) == 10


class TestLinkedListStack:
    def test_push_pop(self):
        s = LinkedListStack()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        assert s.pop() == 1

    def test_peek(self):
        s = LinkedListStack()
        s.push(10)
        assert s.peek() == 10

    def test_is_empty(self):
        s = LinkedListStack()
        assert s.is_empty() is True
        s.push(1)
        assert s.is_empty() is False


class TestValidParenthesis:
    def test_valid(self):
        assert is_valid("()") is True
        assert is_valid("()[]{}") is True
        assert is_valid("{[]}") is True

    def test_invalid(self):
        assert is_valid("(]") is False
        assert is_valid("([)]") is False

    def test_empty(self):
        assert is_valid("") is True

    def test_single_open(self):
        assert is_valid("(") is False

    def test_nested(self):
        assert is_valid("((()))") is True
