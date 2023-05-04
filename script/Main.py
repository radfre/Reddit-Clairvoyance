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
print("")

print(Postmanager.TopBreachPost())
print("")


print(Postmanager.TopCyberPost())
print("")


print(Postmanager.PopularTerms())
print("")


print(Postmanager.affectedOrgs())
print("")


print(Postmanager.SentimentResult())
print("")




##GUI

