import heapq
class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list)
        self.following=defaultdict(set)

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        for posts in self.tweets[userId][-10:]:
            heapq.heappush(heap,posts)

        for f in self.following[userId]:
            for post in self.tweets[f][-10:]:
                heapq.heappush(heap,post)

        res=[]
        for i in range(10):
            if not heap:
                break

            time,tweet=heapq.heappop(heap)
            res.append(tweet)

        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId!=followerId:
            self.following[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)