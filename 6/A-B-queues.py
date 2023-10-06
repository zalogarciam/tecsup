# queue = [3, 1, 2, 5, 7, 9 ,10]

# print(queue)

# # Enqueue
# queue.append(11)
# print(queue)

# # Dequeue
# print(queue.pop(0))
# print(queue)

# # Size
# print('Size:', len(queue))

# # Front
# print('Front:', queue[0])

# # Is Empty
# result =  'Empty' if len(queue) == 0 else 'Not Empty'
# print('Is Empty:', result)

from queue import PriorityQueue

q = PriorityQueue()

q.put((1, 'Lily'))
q.put((1, 'Marcin'))
q.put((0, 'Mary'))
q.put((2, 'John'))
q.put((3, 'Rayan'))

while not q.empty():
    print(q.get())

print('Size:', q.qsize())
print('Empty:', q.empty())
print('Full:', q.full())
