import praw

redditconfig = open("reddit.config", "r")
client_id = redditconfig.readline()[:-1]
client_secret = redditconfig.readline()[:-1]
username = redditconfig.readline()[:-1]
password = redditconfig.readline()[:-1]
token = redditconfig.readline()[:-1]


reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         refresh_token= token,
                         user_agent= "Discord bot!",
                         username= username,
                         password= password)

print(reddit.auth.scopes())
