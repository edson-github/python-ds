"""
Find the sum of elements between k1th and k2th smallest elements
"""


from heapq import heappush, heapify, heappop

heap = [20, 8, 22, 4, 12, 10, 14]
k1 = 3
k2 = 6

heapify(heap)

# extracting min k1 times

for _ in range(k1):
    heappop(heap)

s = sum(heappop(heap) for _ in range(k2 - k1 - 1))
print(s)
