from RedditAPI import RedditAPI
from GUI import GUI
from Postmanager import Postmanager

## read Credentials File

##login


## Begin API
reddit = RedditAPI()

##initialize GUI
Display = GUI()

## Get Posts
Postmanager = reddit.GetPosts()

print(Postmanager.Mentions())
print(Postmanager.TopBreachPost())
print(Postmanager.TopCyberPost())
##GUI

