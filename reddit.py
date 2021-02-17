import praw
import re
import random
import datetime

redditconfig = open("reddit.config", "r")
client_id = redditconfig.readline().rstrip('\n')
client_secret = redditconfig.readline().rstrip('\n')
username = redditconfig.readline().rstrip('\n')
password = redditconfig.readline().rstrip('\n')
token = redditconfig.readline().rstrip('\n')


reddit = praw.Reddit(client_id=client_id
                     , client_secret=client_secret
                     , refresh_token=token
                     , user_agent="Discord bot!"
                     , username=username
                     , password=password)

sys_random = random.SystemRandom()


def searchSub(sub: str, isNSFW: bool):

    subreddit_list = reddit.subreddits.search_by_name(sub, isNSFW, False)

    if len(subreddit_list) == 0:
        return None
    return str(subreddit_list[0])


def getHottestPost(sub: str, isNSFW: int):

    subreddit = reddit.subreddit(sub)

    if subreddit.over18 and not isNSFW:
        raise Exception("This subreddit is NSFW. Try posting ")
        return

    submissions = subreddit.hot(limit=5)

    top_post = list(filter((lambda sub: not sub.stickied and re.findall("(.jpg|.png)$", sub.url)), submissions))

    if len(top_post) == 0:
        raise Exception("Couldn't find any submissions")

    return top_post[0].url


def getRandomPost(sub: str,  isNSFW: int):
    subreddit = reddit.subreddit(sub)

    if subreddit.over18 and not isNSFW:
        raise Exception("This subreddit is NSFW")

    random_cap = random.randrange(start=0, stop=500)

    tstart = datetime.datetime.now()

    submissions = subreddit.hot(limit=random_cap)

    random_post = list(filter((lambda sub: not sub.stickied and re.findall("(.jpg|.png)$", sub.url)), submissions))[-1]

    tend = datetime.datetime.now()

    duration = (tend - tstart).total_seconds()
    print("Request took {} seconds for searching {} posts".format(duration, random_cap))

    return random_post.url


if __name__ == "__main__":
    getHottestPost("prequelmemes")
