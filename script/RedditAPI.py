import praw
from Read import Read
from Postmanager import Postmanager


class RedditAPI:
    def __init__(self):
        read = Read('../Credential.txt')
        self.reddit = praw.Reddit(client_id=read.client_ID(),
                                  client_secret=read.client_secret(),
                                  user_agent=read.user_agent(), )
        self.subreddits = [self.reddit.subreddit('cybersecurity'), self.reddit.subreddit('netsec'),
                           self.reddit.subreddit('hacking'), self.reddit.subreddit('malware'),
                           self.reddit.subreddit('threatintelligence'), self.reddit.subreddit('cybercrime'),
                           self.reddit.subreddit('antivirus')]
    def GetPosts(self):
        manager = Postmanager()
        PostNum=0
        for subreddit in self.subreddits:
            top_subreddit = subreddit.hot(limit=1000)
            for submission in top_subreddit:
                if not submission.stickied:
                    manager.add_posts(PostNum, subreddit.display_name, submission.title, submission.selftext, (submission.ups - submission.downs), submission.author)
                    ##manager.add_User(submission.author, submission.author.comment_karma)
                    PostNum+=1
        return manager

    def topofall(self):
        Text = ""
        for subreddit in self.subreddits:
            top_subreddit = subreddit.hot(limit=100)
            for submission in top_subreddit:
                if not submission.stickied:

                    Text += ('sub: {}\n\tTitle: {}\n\t\t points: {}\n\n'.format(subreddit.display_name, submission.title,
                                                                              (submission.ups - submission.downs)))
        return Text
