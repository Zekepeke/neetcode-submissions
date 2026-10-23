class MedianFinder:

    def __init__(self):
        self.small = []  # max heap (negated), lower half
        self.large = []  # min heap, upper half

    def addNum(self, num: int) -> None:
        # 1. Put it on the correct side
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # 2. Fix the sizes (small may have 1 extra, never more)
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2