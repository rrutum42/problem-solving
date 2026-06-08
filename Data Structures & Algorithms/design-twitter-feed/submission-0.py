class Twitter:
    # O(nlogn), O(U*f + U*t + k)
    def __init__(self):
        self.count = 0 
        # O(number_of_users * max_followees_per_user) = O(U*f)
        self.follows = defaultdict(set) # user -> set of followees
        # O(number_of_users * max_tweets_per_users) = O(U*t)
        self.tweetMap = defaultdict(list) # user -> [time,tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1

    # O(nlogn) 
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = [] # O(k) = number of followee ids associated with user
        self.follows[userId].add(userId)
        
        for followee in self.follows[userId]:
            if followee in self.tweetMap:
                last_index = len(self.tweetMap[followee]) -1
                count, tweetId = self.tweetMap[followee][last_index]
                next_index_to_look_at = last_index -1
                heapq.heappush(minHeap, [count, tweetId, followee, next_index_to_look_at])
        '''
Pop: The heap gives you the latest global tweet. You add it to res.

Track: Suppose that tweet belonged to Alice, and it was her 5th tweet (index = 4).

Push Next: Since we just took Alice's newest tweet, her next newest tweet (index - 1 = 3) now becomes a candidate. We fetch it from self.tweetMap and push it into the heap.

The heap reorganizes itself, and the loop repeats until we have gathered 10 tweets or run completely out of tweets.
        '''
        while minHeap and len(res) < 10:
            count,tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)