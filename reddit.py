import praw
import re

redditconfig = open("reddit.config", "r")
client_id = redditconfig.readline().rstrip('\n')
client_secret = redditconfig.readline().rstrip('\n')
username = redditconfig.readline().rstrip('\n')
password = redditconfig.readline().rstrip('\n')
token = redditconfig.readline().rstrip('\n')


reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     refresh_token= token,
                     user_agent= "Discord bot!",
                     username= username,
                     password= password)

def getHottestPost(sub: str):
    subreddit = reddit.subreddit(sub)

    submissions = subreddit.hot(limit=5)

    top_post = list(filter((lambda sub: not sub.stickied and re.findall("(.jpg|.png)$" ,sub.url)), submissions))

    if len(top_post) == 0:
        raise Exception("Couldn't find any submissions")

    print(top_post[0].url)
    return top_post[0].url

if __name__ == "__main__":
    getHottestPost("prequelmemes")
