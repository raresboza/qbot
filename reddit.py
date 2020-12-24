import praw

redditconfig = open("reddit.config", "r")
client_id = redditconfig.readline()
client_secret = redditconfig.readline()
username = redditconfig.readline()
password = redditconfig.readline()
token = redditconfig.readline()


reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         refresh_token= token,
                         user_agent= "Discord bot!",
                         username= username,
                         password= password)

print(reddit.auth.scopes())
