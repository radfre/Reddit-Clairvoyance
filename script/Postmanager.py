from collections import Counter
import re
from nameparser import HumanName
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob


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

        return ('Total Posts: {}\n'
                'Mentions of Cyberattacks:   {}\n'
                'Mentions of Data Breaches:   {}'.format(len(self.posts), breachMention, cybrMention))

    def TopBreachPosts(self):
        breach_posts = [post for post in self.posts if
                        any(synonym in post.title or synonym in post.desc for synonym in self.breach_synonyms)]
        sorted_breach_posts = sorted(breach_posts, key=lambda post: post.points, reverse=True)
        top_breach_posts = sorted_breach_posts[:2]
        return f"The top 2 posts with 'Breach' in the title or description are: \n1. {top_breach_posts[0].title} with {top_breach_posts[0].points} points\n2. {top_breach_posts[1].title} with {top_breach_posts[1].points} points"

    def TopCyberPost(self):
        cyber_posts = [post for post in self.posts if
                       any(synonym in post.title or synonym in post.desc for synonym in self.cyberattack_synonyms)]
        top_cyber_post = max(cyber_posts, key=lambda post: post.points)
        return f"The top post with 'Cyber' in the title or description has {top_cyber_post.points} \n\tpoints and is " \
               f"titled:   {top_cyber_post.title}. "

    def TopUser(self):
        top_user = max(self.users, key=lambda user: user.points)
        return f"The top user is '{top_user.username}' with {top_user.points} points."

    def PopularTerms(self):
        all_text = ' '.join([f"{post.title} {post.desc}" for post in self.posts])
        pattern = re.compile(r'\w+')
        words = pattern.findall(all_text.lower())

        common_words = set(stopwords.words('english'))
        bad_words = {'bad'}
        filtered_words = [word for word in words if word not in common_words and word not in bad_words]
        common_filtered_words = Counter(filtered_words).most_common(25)

        return [word[0] for word in common_filtered_words]

    def affected_orgs(self):
        orgs = set()
        for post in self.posts:
            if 'breach' in post.title.lower() or 'breach' in post.desc.lower():
                # Identify affected organizations from the post's description or title
                # and add them to the set
                orgs.update([str(HumanName(org.strip())) for org in
                             re.findall(r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)', post.desc + post.title)])
            if 'cyber' in post.title.lower() or 'cyber' in post.desc.lower():
                # Identify affected organizations from the post's description or title
                # and add them to the set
                orgs.update([str(HumanName(org.strip())) for org in
                             re.findall(r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)', post.desc + post.title)])
        return list(orgs)

    def SentimentResult(self):
        sentiments = []
        for post in self.posts:
            blob = TextBlob(post.desc)
            sentiment = blob.sentiment.polarity
            if sentiment <= -0.8:  # only show posts with negative sentiment score less than or equal to -0.5
                sentiments.append((post.title, post.desc, sentiment))
        top_3 = sorted(sentiments, key=lambda x: x[2])[:3]  # sort in ascending order
        output_list = []
        for post in top_3:
            output_list.append(f'Title: {post[0]}\nDescription: {post[1]}\nSentiment: {post[2]}')
        return output_list


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
