import operator


s = input("postfix expression?")
queue = Queue(queue)
stack = Stack(stack)
ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.div,
        }
for c in s:
    queue.enqueue(queue,c)
    
while queue.isEmpty == False:
    obj = queue.dequeue(queue)
    if obj == '/' or obj == '*' or obj == '+' or obj == '-':
        x = int(stack.pop(stack))
        y = int(stack.pop(stack))
        x = ops[obj](x,y)
        stack.push(stack,x)
    else:
        stack.push(stack,obj)

print (stack.pop(stack))
    






class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
