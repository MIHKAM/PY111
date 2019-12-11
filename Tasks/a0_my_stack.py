"""
My little Stack
"""
from typing import Any

stack = []

def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global stack
	stack.append(elem)



def pop() -> Any:
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global stack
	if len(stack) != 0:
		return stack.pop()
	else:
		return None




def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	global stack
	if ind <= len(stack):
		return stack[-ind-1]
	else:
		return None


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	stack.clear()
	return None
