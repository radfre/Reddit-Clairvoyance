from RedditAPI import RedditAPI
from GUI import GUI
from Postmanager import Postmanager
from Login import LoginWindow

while True:
    try:
        login_window = LoginWindow()
        login_window.show()
        print('logging in....')
        reddit = RedditAPI(login_window.client_id, login_window.client_secret, login_window.user_agent)

        break
    except Exception as e:
        print(f'Error: Failed to log in. Retrying in 5 seconds... {e}')

##initialize GUI
Display = GUI()

## Get Posts
Postmanager = reddit.GetPosts()

## Load data into GUI
Display.loadMention(Postmanager.Mentions())
Display.loadBreachPost(Postmanager.TopBreachPosts())
Display.loadCyberPost(Postmanager.TopCyberPosts())
Display.loadPopTerm(Postmanager.PopularTerms())
Display.loadAffeceted(Postmanager.affected_orgs())
Display.loadSentient(Postmanager.SentimentResult())

## Run GUI
Display.window.mainloop()

# print(Postmanager.Mentions())
# print(Postmanager.TopBreachPosts())
# print(Postmanager.TopCyberPost())
# print(Postmanager.PopularTerms())
# print(Postmanager.affected_orgs())
# print(Postmanager.SentimentResult())
