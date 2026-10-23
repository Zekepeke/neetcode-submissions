class Twitter:

    def __init__(self):
        self.time = 0
        self.k = 10
        self.tweetMap = {}
        self.follow_map = {}

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if userId in self.tweetMap:
            self.tweetMap[userId].append((-self.time, tweetId))
        else:
            top_post = []
            top_post.append((-self.time, tweetId))
            self.tweetMap[userId] = top_post

    
    def getNewsFeed(self, userId: int) -> List[int]:
        us = self.follow_map.get(userId, set()) | {userId}
        heap = []
        for u in us:
            if u in self.tweetMap:
                heap.extend(self.tweetMap[u])
        heapq.heapify(heap)
        res = []
        while heap and len(res) < self.k:
            res.append(heapq.heappop(heap)[1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].add(followeeId)
        else:
            set_f = set()
            set_f.add(followeeId)
            self.follow_map[followerId] = set_f
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map:
            self.follow_map[followerId].discard(followeeId)
        
