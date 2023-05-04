from RedditAPI import RedditAPI
from GUI import GUI

## read Credentials File

##login


## Begin API
reddit = RedditAPI()

##initialize GUI
Display = GUI()

## begin Reddit API
TopPosts = reddit.topofall()


##GUI

Display.display_top_posts(TopPosts)