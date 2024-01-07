import sys
from collections import deque


if len(sys.argv) < 2:
    print("Usage: c.py <FileName>")
    sys.exit(1)

stack = deque()

def add():
    global stack
    op1 = stack.pop()
    op2 = stack.pop()
    stack.append(op1 + op2)
    return

def sub():
    op1 = stack.pop()
    op2 = stack.pop()
    stack.append(op1 - op2)
    return

def print_stack():
    global stack
    print(stack.pop())

def process_token(token):
    global stack
    if token.isdigit():
        stack.append(int(token))
    if token == "add":
        add()
    elif token == "sub":
        sub()
    elif token == "print":
        print_stack()


file_name = sys.argv[1]
#print("Interpreting " + file_name) do not really need to print filename
with open(file_name, 'r') as file:
    file_content = file.read()
    tokens = file_content.split()
    for token in tokens:
        process_token(token)

