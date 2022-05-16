"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


from operator import le


class Stack:
    def __init__(self):
        self.items = []

    def __getattr__(self, attr: str):
        if attr == 'is_empty':
            return not self.items
        elif attr == 'peek':
            return self.items[-1]
        elif attr == 'size':
            return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    # def size(self):
    #     return len(self.items)

    def __str__(self) -> str:
        return str(self.items)
    
if __name__=='__main__':
    s = Stack()
    print(s)
    print(s.is_empty)
    print(s.peek)
    print(s.size)
    
