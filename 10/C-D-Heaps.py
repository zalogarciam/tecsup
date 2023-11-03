import heapq

values = [5,1,3,7,4,2]

heapq.heapify(values)

print(values)

heapq._heapify_max(values)

print(values)

heapq.heappush(values, 6)
print(values)
print(heapq.heappop(values))

print(heapq.nlargest(2, values))

print(heapq.nsmallest(2, values))