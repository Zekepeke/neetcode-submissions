class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = {}

        for n in nums:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 1
        
        h = []

        for knum, m in hm.items():
            h.append((-m,knum))

        heapq.heapify(h)

        res = []
        for i in range(k):
            m, knum = heapq.heappop(h)
            res.append(knum)
        return res


    


        