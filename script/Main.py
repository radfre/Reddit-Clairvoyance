from RedditAPI import RedditAPI
from GUI import GUI
from Postmanager import Postmanager
from Login import LoginWindow

## read Credentials File
login_window = LoginWindow()
login_window.show()

## Login to Reddit API
reddit = RedditAPI(client_id=login_window.client_id,
                   client_secret=login_window.client_secret,
                   user_agent=login_window.user_agent)

## Begin API
reddit = RedditAPI()

##initialize GUI
Display = GUI()

## Get Posts
Postmanager = reddit.GetPosts()

print(Postmanager.Mentions())
print("")

print(Postmanager.TopBreachPosts())
print("")


print(Postmanager.TopCyberPost())
print("")


print(Postmanager.PopularTerms())
print("")


print(Postmanager.affected_orgs())
print("")


print(Postmanager.SentimentResult())
print("")




##GUI

