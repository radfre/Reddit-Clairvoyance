from RedditAPI import RedditAPI
from GUI import GUI

## read Credentials File

##login


## Begin API
reddit = RedditAPI()

## begin Reddit API
TopPosts = reddit.topofall()


##GUI
Display = GUI()

Display.display_top_posts(TopPosts)