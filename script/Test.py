## this is a test file for working in python  reddit api


import praw
from Read import Read

read = Read('../Credential.txt')

reddit = praw.Reddit(client_id=read.client_ID(),
                     client_secret=read.client_secret(), password=read.password(),
                     user_agent=read.user_agent(), username=read.user_name())

subreddit = reddit.subreddit('python')
hot_python = subreddit.new()

hot_python = subreddit.hot(limit=100)
n =0;
for submission in hot_python:
    if not submission.stickied:
        n += 1;
        print('num: {} \n Title: {}\n\t ups: {}'.format(n, submission.title, submission.ups))