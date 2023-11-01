import heapq

values = [5,1,3,7,4,2]

heapq.heapify(values)

print(values)

heapq.heappush(values, 6)

print(values)

print(heapq.heappop(values))
print(values)

print(heapq.nsmallest(3, values))
print(heapq.nlargest(3, values))