class Postmanager:
    def __init__(self):
        self.posts = []
        self.users = []

    def add_posts(self, Number, Subreddit, Title, Desc, Points, User):
        self.posts.append(Post(Number, Subreddit, Title, Desc, Points, User))

    def add_User(self,Username, Points ):
        self.users.append(User(Username, Points))

    def mentions(self):
        print('hello')

    def TopBreachPost(self):
        print('hello')

    def TopCyberPost(self):
        print('hello')

    def TopUser(self):
        print('hello')



class Post:
    def __init__(self, Number, Subreddit, Title, Desc, Points, Username):
        self.number = Number
        self.subreddit = Subreddit
        self.title = Title
        self.desc = Desc
        self.points = Points
        self.user = User


class User:
    def __init__(self, Username, Points):
        self.username = Username
        self.points = Points
