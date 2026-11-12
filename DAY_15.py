#QN_183
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
popped_element=stack.pop()
print(popped_element)
print(stack)


#QN_184

expression = "{[()]}"
stack = []

pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

balanced = True

for char in expression:

    if char in '({[':
        stack.append(char)

    else:
#if not stack: means check whether the stack is empty.
        if not stack:
            balanced = False
            break

        top = stack.pop()

        if top != pairs[char]:
            balanced = False
            break

if len(stack) != 0:
    balanced = False

if balanced:
    print("Balanced")
else:
    print("Not Balanced")


#QN_185

string = "hello"
stack = []

popped_string = []

for ch in string:
    stack.append(ch)


#while the stack is NOT empty (True).
while stack:
    popped_element = stack.pop()
    popped_string.append(popped_element)

print(stack)
print(popped_string)
print("".join(popped_string))


#QN_186

arr = [4, 5, 2, 25]

stack = []

result = [-1] * len(arr)

for i in range(len(arr)):

    while stack and arr[i] > arr[stack[-1]]:

        index = stack.pop()

        result[index] = arr[i]

    stack.append(i)

print(result)


#QN_187
queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue
removed = queue.pop(0)

print("Dequeued:", removed)
print("Queue:", queue)


#QN_188
size = 3
queue = [None] * size

front = -1
rear = -1

# Enqueue 1
if (rear + 1) % size != front:
    if front == -1:
        front = 0
    rear = (rear + 1) % size
    queue[rear] = 1

# Enqueue 2
if (rear + 1) % size != front:
    rear = (rear + 1) % size
    queue[rear] = 2

# Enqueue 3
if (rear + 1) % size != front:
    rear = (rear + 1) % size
    queue[rear] = 3

# Dequeue
removed = queue[front]
queue[front] = None

if front == rear:
    front = rear = -1
else:
    front = (front + 1) % size

# Enqueue 4
if (rear + 1) % size != front:
    if front == -1:
        front = 0
    rear = (rear + 1) % size
    queue[rear] = 4

print("Queue:", [queue[(front + i) % size] for i in range(size) if front != -1 and queue[(front + i) % size] is not None])



#QN_189
stack1 = []
stack2 = []


#stack1 → Stores the incoming elements.
# stack2 → Helps remove elements in the correct queue order.


# Enqueue operation
def enqueue(value):
    stack1.append(value)

# Dequeue operation
def dequeue():

    if not stack2:
        while stack1:
            stack2.append(stack1.pop())

    if not stack2:
        return "Queue is empty"

    return stack2.pop()


# Enqueue elements
enqueue(1)
enqueue(2)
enqueue(3)

# Dequeue
print("Dequeued:", dequeue())

