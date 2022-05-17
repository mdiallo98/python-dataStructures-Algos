from collections import defaultdict
from sqlite3 import Timestamp


class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.FollowerMap = defaultdict(set)
        self.Tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # whenever a user posts a tweet we need a identifier which will be the userID and we also need the tweetID to differentiate between tweets. Furthere more we need our timestamp to organize the tweets in terms of when they were created
        self.Tweets[userId].append([self.timestamp, tweetId])
        # we then decrement the timestamp since we are using a min heap
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        min_heap = []

        for follower in self.FollowerMap[userId]:
            if follower in self.Tweets:
                index = len(self.Tweets[follower])-1
                Timestamp, tweets = self.Tweets[follower][index]

    def follow(self, followerId: int, followeeId: int) -> None:
        # how would we follow a user? Well we would create a connection between one user and the other users they want to follow.
        self.FollowerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.FollowerMap[followerId]:
            self.FollowerMap[followerId].remove(followeeId)
