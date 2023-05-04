## this is a test file for working in python  reddit api


import praw
from Read import Read

read = Read('../Credential.txt')

reddit = praw.Reddit(client_id=read.client_ID(),
                     client_secret=read.client_secret(),
                     user_agent=read.user_agent(), )

subreddit = reddit.subreddit('python')
top_subreddit = subreddit.new()
top_subreddit = subreddit.top(limit=1)
n =0;


for submission in top_subreddit:
    if not submission.stickied:
        n += 1;
        print('num: {} \n Title: {}\n\t points: {}'.format(n, submission.title, (submission.ups - submission.downs)))