import praw
from Read import Read

class RedditAPI:
    def __init__(self):
        read = Read('../Credential.txt')
        self.reddit = praw.Reddit(client_id=read.client_ID(),
                                  client_secret=read.client_secret(),
                                  user_agent=read.user_agent(), )
        self.subreddits = [self.reddit.subreddit('cybersecurity'), self.reddit.subreddit('netsec'),
                           self.reddit.subreddit('hacking'), self.reddit.subreddit('malware'),
                           self.reddit.subreddit('threatintelligence'), self.reddit.subreddit('cybercrime'), self.reddit.subreddit('antivirus')]

    def topofall(self):
        Text = ""
        for subreddit in self.subreddits:
            top_subreddit = subreddit.hot(limit=2)
            for submission in top_subreddit:
                if not submission.stickied:
                    Text += ('sub: {}\tTitle: {}\t points: {}\n'.format(subreddit.display_name, submission.title, (submission.ups - submission.downs)))
        return Text
