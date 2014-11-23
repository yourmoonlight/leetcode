class MinStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)
        if len(self.stack2) == 0 or x <= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self):
        pop = self.stack1[-1]
        self.stack1.pop()
        if pop == self.stack2[-1]:
            self.stack2.pop()

    def top(self):
        return self.stack1[-1]

    def min_elem(self):
        return self.stack2[-1]
