import praw
from Read import Read
from Postmanager import Postmanager


class RedditAPI:
    def __init__(self, client_ID="", client_secret="", user_agent=""):
        if client_ID:
            self.reddit = praw.Reddit(client_id=client_ID(),
                                      client_secret=client_secret,
                                      user_agent=user_agent, )
        else:
            read = Read('../Credential.txt')
            self.reddit = praw.Reddit(client_id=read.client_ID(),
                                      client_secret=read.client_secret(),
                                      user_agent=read.user_agent(), )
            self.subreddits = [self.reddit.subreddit('cybersecurity'), self.reddit.subreddit('netsec'),
                               self.reddit.subreddit('hacking'), self.reddit.subreddit('malware'),
                               self.reddit.subreddit('threatintelligence'), self.reddit.subreddit('cybercrime'),
                               self.reddit.subreddit('antivirus'), self.reddit.subreddit('websecurity'),
                               self.reddit.subreddit('blackhat'), self.reddit.subreddit('infosecurity'),
                               self.reddit.subreddit('Privacy'), self.reddit.subreddit('Information_Security'), self.reddit.subreddit('intelligence'),
                               self.reddit.subreddit('ComputerSecurity')]


    def GetPosts(self, limit=100, time_filter='year'):
        manager = Postmanager()
        PostNum = 0
        for subreddit in self.subreddits:
            top_subreddit = subreddit.top(limit=limit, time_filter=time_filter)
            print(subreddit)
            for submission in top_subreddit:

                if not submission.stickied:
                    manager.add_posts(PostNum, subreddit.display_name, submission.title, submission.selftext,
                                      submission.url,
                                      (submission.ups - submission.downs), submission.author)
                    ##manager.add_User(submission.author, submission.author.comment_karma)
                    PostNum += 1

        return manager

    def topofall(self):
        Text = ""
        for subreddit in self.subreddits:
            top_subreddit = subreddit.hot(limit=100)
            for submission in top_subreddit:
                if not submission.stickied:
                    Text += (
                        'sub: {}\n\tTitle: {}\n\t\t points: {}\n\n'.format(subreddit.display_name, submission.title,
                                                                           (submission.ups - submission.downs)))
        return Text
