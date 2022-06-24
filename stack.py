class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) > 0:
            return True
        else:
            return False

    def push(self, x):
        return self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return print(len(self.stack))


def balance(x):
    stack = Stack()

    a = 0
    b = 0

    for y in x:
        if y == '(':
            a += 1
        if y == '[':
            a += 1
        if y == '{':
            a += 1

        if y == ')':
            b += 1
        if y == ']':
            b += 1
        if y == '}':
            b += 1

        stack.push(y)

    if a == b:
        return print('Сбалансированно')
    else:
        return print('Несбалансированно')

    # if s.stack.count('(') == s.stack.count(')')\
    #         and s.stack.count('[') == s.stack.count(']')\
    #         and s.stack.count('{') == s.stack.count('}'):
    #     return print('Сбалансированно')
    # else:
    #     return print('Несбалансированно')


skob1 = '(((([{}]))))'
skob2 = '[([])((([[[]]])))]{()}'
skob3 = '{{[()]}}'

skob4 = '}{}'
skob5 = '{{[(])]}}'
skob6 = '[[{())}]'

if __name__ == '__main__':
    balance(skob1)
