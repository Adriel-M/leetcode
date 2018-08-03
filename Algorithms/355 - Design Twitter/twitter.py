class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_tweets = {}
        self.follows = {}
        self.tweets = {}
        self.tweet_count = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId in self.user_tweets:
            self.user_tweets[userId].append(tweetId)
        else:
            self.user_tweets[userId] = [tweetId]
        self.tweet_count += 1
        self.tweets[tweetId] = self.tweet_count

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tweets = self.user_tweets.get(userId, [])
        for follows in self.follows.get(userId, []):
            tweets = tweets + self.user_tweets.get(follows, [])
        tweets = list(set(tweets))
        tweets.sort(key=lambda x: self.tweets[x], reverse=True)
        return tweets[:10]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = set([followeeId])

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        user_follows = self.follows.get(followerId, set())
        user_follows.discard(followeeId)
