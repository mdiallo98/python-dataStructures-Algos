from collections import defaultdict
import heapq
from sqlite3 import time_send


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

        for user in self.FollowerMap[userId]:
            if user in self.Tweets:
                index = len(self.Tweets[user])-1
                time_send, tweets = self.Tweets[user][index]
                min_heap.append([time_send, tweets, user, index-1])

        heapq.heapify(min_heap)

        while min_heap and len(news_feed) < 10:
            time_send, tweets, user, index = heapq.heappop(min_heap)
            news_feed.append(tweets)
            if index >= 0:
                time_send, tweets = self.Tweets[user][index]
                heapq.heappush(min_heap, [time_send, tweets, user, index-1])
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # how would we follow a user? Well we would create a connection between one user and the other users they want to follow.
        self.FollowerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.FollowerMap[followerId]:
            self.FollowerMap[followerId].remove(followeeId)
