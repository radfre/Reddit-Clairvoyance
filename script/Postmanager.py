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

    def add_posts(self, Number, Subreddit, Title, Desc, Points, Link, User):
        self.posts.append(Post(Number, Subreddit, Title, Desc, Points, Link, User))

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
        if not top_breach_posts:
            return "No posts found with 'Breach' in the title or description."
        elif len(top_breach_posts) == 1:
            return f"The top post with 'Breach' in the title or description has {top_breach_posts[0].points} points:\n\n titled: {top_breach_posts[0].title}\n desc:{top_breach_posts[0].desc}\n\n\tReddit Link: {top_breach_posts[0].link}."
        else:
            return f"The top 2 posts with 'Breach' in the title or description are:\n\n\n1. {top_breach_posts[0].title}\nPoints: {top_breach_posts[0].points} \ndesc:{top_breach_posts[0].desc}\n\n\tReddit Link {top_breach_posts[0].link}\n\n\n\n2.\n {top_breach_posts[1].title}\n Points: {top_breach_posts[1].points} \ndesc:{top_breach_posts[1].desc}\n\nLink: {top_breach_posts[1].link}. "

    def TopCyberPosts(self):
        cyber_posts = [post for post in self.posts if
                       any(synonym in post.title or synonym in post.desc for synonym in self.cyberattack_synonyms)]
        sorted_cyber_posts = sorted(cyber_posts, key=lambda post: post.points, reverse=True)
        top_cyber_posts = sorted_cyber_posts[:2]
        if not top_cyber_posts:
            return "No posts found with 'Cyber' in the title or description."
        elif len(top_cyber_posts) == 1:
            return f"The top post with 'Cyber' in the title or description has {top_cyber_posts[0].points} points:\n titled: {top_cyber_posts[0].title}\n desc:{top_cyber_posts[0].desc}\n\n\tReddit Link {top_cyber_posts[0].link}."
        else:
            return f"The top 2 posts with 'Cyber' in the title or description are:\n\n\n1. {top_cyber_posts[0].title}\nPoints: {top_cyber_posts[0].points} \ndesc:{top_cyber_posts[0].desc}\n\n\tReddit Link {top_cyber_posts[0].link}\n\n\n\n2.\n {top_cyber_posts[1].title}\n Points: {top_cyber_posts[1].points} \ndesc:{top_cyber_posts[1].desc}\n\nLink: {top_cyber_posts[1].link}. "

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
        final =[word[0] for word in common_filtered_words]
        final[:0] = ['Most Common Words\n']
        return final

    def affected_orgs(self):
        orgs = set()
        for post in self.posts:
            if 'breach' in post.title.lower() or 'breach' in post.desc.lower():
                # Identify affected organizations from the post's description or title
                # and add them to the set
                orgs.update([str(HumanName(org.strip())) for org in
                             re.findall(r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)', post.desc + post.title)])

        final = list(orgs)
        final[:0] = ['Affected Organizations\n']
        return final

    from textblob import TextBlob

    def SentimentResult(self):
        sentiments = []
        for post in self.posts:
            blob = TextBlob(post.desc)
            sentiment = blob.sentiment.polarity
            sentiments.append((post.title, post.desc, sentiment, post.link))
        top_5 = sorted(sentiments, key=lambda x: x[2])[:5]
        output = 'The top 5 most negative posts using Sentiment Analysis and Natural Language Processing:\n\n\n'
        for i, post in enumerate(top_5):
            output += f'{i + 1}. \tTitle: {post[0]}\n\nDescription: {post[1]}\n\n\tSentiment: {post[2]}\n\tLink: {post[3]}\n\n\n\n'
        return output


class Post:
    def __init__(self, Number, Subreddit, Title, Desc,
                 Link, Points, Username):
        self.number = Number
        self.subreddit = Subreddit
        self.title = Title
        self.desc = Desc
        self.link = Link
        self.points = Points
        self.user = Username


class User:
    def __init__(self, Username, Points):
        self.username = Username
        self.points = Points
