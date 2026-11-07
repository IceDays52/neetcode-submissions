class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeapq = [] 

        for x,y in points:
               dist = (x**2) + (y**2)
               minHeapq.append([dist, x , y])

        heapq.heapify(minHeapq)

        res = []

        while k > 0:
            dist , x , y = heapq.heappop(minHeapq)
            res.append([x,y])
            k -= 1

        return res




