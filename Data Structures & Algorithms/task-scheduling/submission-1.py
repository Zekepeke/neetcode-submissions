class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-c for c in counts.values()]
        heapq.heapify(max_heap)
        t = 0
        queue = deque()
        while max_heap or queue:
            t += 1 
            if max_heap:
                freq = -heapq.heappop(max_heap)
                freq -= 1
                if freq > 0:
                    queue.append((freq, t + n))
            if queue:
                prev_freq, prev_t = queue[0]
                if prev_t <= t:
                    heapq.heappush(max_heap, -prev_freq)
                    queue.popleft()


            

        return t
        