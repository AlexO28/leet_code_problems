# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
# Implement the Twitter class:
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


class Twitter:
    def __init__(self):
        self.twitter = {}
        self.followers = {}
        self.tweets = {}
        self.max_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.twitter:
            self.twitter[userId] = self.twitter[userId][:10] 
            self.twitter[userId].insert(0, self.max_count)
        else:
            self.twitter[userId] = [self.max_count]
        self.tweets[self.max_count] = tweetId
        self.max_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.twitter:
            tweets = []
        else:
            tweets = self.twitter[userId].copy()
        if userId in self.followers:
            for follower in self.followers[userId]:
                if follower in self.twitter:
                    tweets.extend(self.twitter[follower].copy())
        tweets = list(set(tweets))
        tweets.sort(reverse = True)
        counts = []
        for tweet in tweets[:10]:
            counts.append(self.tweets[tweet])
        return counts
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = [followeeId]
        else:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)
                if len(self.followers[followerId]) == 0:
                    del self.followers[followerId]

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
