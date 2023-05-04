class Postmanager:

    def __init__(self):
        self.posts = []
        self.users = []

        # Synonyms for "Breach"
        self.breach_synonyms = ["Breach", "Security Breach", "Data Breach", "Compromise", "Intrusion", "Security lapse",
                                "Data leak", "Unauthorized access", "Exploit", "Violation", "Infraction", "Trespass",
                                "Incursion"]

        # Synonyms for "CyberAttack"
        self.cyberattack_synonyms = ["CyberAttack", "Cyber Attack", "Hack", "Malware attack", "Cyber intrusion",
                                     "Denial-of-service attack", "Phishing attack", "Ransomware attack",
                                     "Advanced persistent threat", "Cyber espionage", "Social engineering attack",
                                     "Cyber warfare"]

    def add_posts(self, Number, Subreddit, Title, Desc, Points, User):
        self.posts.append(Post(Number, Subreddit, Title, Desc, Points, User))

    def add_User(self, Username, Points):
        self.users.append(User(Username, Points))

    def Mentions(self):

        # Count mentions of breach and cyberattack synonyms
        breachMention = 0
        cybrMention = 0
        for post in self.posts:
            for synonym in self.breach_synonyms:
                if synonym in post.title or synonym in post.desc:
                    breachMention += 1
                    break  # exit loop once a synonym is found
            for synonym in self.cyberattack_synonyms:
                if synonym in post.title or synonym in post.desc:
                    cybrMention += 1
                    break  # exit loop once a synonym is found

        return ('Mentions of Cyberattacks:   {}\n'
                'Mentions of Data Breaches:   {}'.format(breachMention, cybrMention))

    def TopBreachPost(self):
        breach_posts = [post for post in self.posts if
                        any(synonym in post.title or synonym in post.desc for synonym in self.breach_synonyms)]
        top_breach_post = max(breach_posts, key=lambda post: post.points)
        return f"The top post with 'Breach' in the title or description has {top_breach_post.points} \n\tpoints and " \
               f"is titled:   {top_breach_post.title}. "

    def TopCyberPost(self):
        cyber_posts = [post for post in self.posts if
                       any(synonym in post.title or synonym in post.desc for synonym in self.cyberattack_synonyms)]
        top_cyber_post = max(cyber_posts, key=lambda post: post.points)
        return f"The top post with 'Cyber' in the title or description has {top_cyber_post.points} \n\tpoints and is " \
               f"titled:   {top_cyber_post.title}. "

    def TopUser(self):
        top_user = max(self.users, key=lambda user: user.points)
        return f"The top user is '{top_user.username}' with {top_user.points} points."


class Post:
    def __init__(self, Number, Subreddit, Title, Desc, Points, Username):
        self.number = Number
        self.subreddit = Subreddit
        self.title = Title
        self.desc = Desc
        self.points = Points
        self.user = Username


class User:
    def __init__(self, Username, Points):
        self.username = Username
        self.points = Points
