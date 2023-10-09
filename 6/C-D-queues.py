queue = []

# Enqueue
queue.append(1)
queue.append(4)
queue.append(2)
queue.append(7)
queue.append(0)

# Dequeue
# print('Deleted:', queue.pop(0))

# # Front
# print('Front:', queue[0])

# # Size
# print('Size', len(queue))

# # Is Empty
# print('Is Empty: ', len(queue) == 0)

# print(queue)


from queue import PriorityQueue

priority_queue = PriorityQueue()
priority_queue.put(1, 'Lily') # 2
priority_queue.put(1, 'Marcin') # 3
priority_queue.put(0, 'Mary') # 1
priority_queue.put(2, 'John') # 5
priority_queue.put(1, 'Emily') # 4

while priority_queue:
    print(priority_queue.get())
