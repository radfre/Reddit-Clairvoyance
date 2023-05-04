from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Reddit API App")
        self.window.geometry("1000x600")

        self.tabs = Notebook(self.window)
        self.mention_tab = Frame(self.tabs)
        self.breach_post_tab = Frame(self.tabs)
        self.cyber_post_tab = Frame(self.tabs)
        self.popular_term_tab = Frame(self.tabs)
        self.affected_orgs_tab = Frame(self.tabs)
        self.sentiment_tab = Frame(self.tabs)

        style = ttk.Style()
        style.configure('TNotebook.Tab', font=('Helvetica', 14))

        self.tabs.add(self.mention_tab, text="Mentions")
        self.tabs.add(self.breach_post_tab, text="Top Breach Posts")
        self.tabs.add(self.cyber_post_tab, text="Top Cyber Posts")
        self.tabs.add(self.popular_term_tab, text="Popular Terms")
        self.tabs.add(self.affected_orgs_tab, text="Affected Organizations")
        self.tabs.add(self.sentiment_tab, text="Sentiment Analysis")

        self.tabs.pack(expand=1, fill="both")

        self.mention_text = Text(self.mention_tab, height=200, width=300)
        self.mention_text.pack(expand=1, fill="both", padx=10, pady=10)

        self.breach_post_text = Text(self.breach_post_tab, height=200, width=300)
        self.breach_post_text.pack(expand=1, fill="both", padx=10, pady=10)

        self.cyber_post_text = Text(self.cyber_post_tab, height=200, width=300)
        self.cyber_post_text.pack(expand=1, fill="both", padx=10, pady=10)

        self.popular_term_list = Listbox(self.popular_term_tab, height=200, width=300)
        self.popular_term_list.pack(expand=1, fill="both", padx=10, pady=10)

        self.affected_orgs_list = Listbox(self.affected_orgs_tab, height=400, width=100)
        self.affected_orgs_list.pack(expand=1, fill="both", padx=10, pady=10)

        self.sentiment_text = Text(self.sentiment_tab, height=200, width=300)
        self.sentiment_text.pack(expand=1, fill="both", padx=10, pady=10)

    def loadMention(self, mentionText):
        self.mention_text.insert(END, mentionText)

    def loadBreachPost(self, breachPostText):
        self.breach_post_text.insert(END, breachPostText)

    def loadCyberPost(self, cyberPostText):
        self.cyber_post_text.insert(END, cyberPostText)

    def loadPopTerm(self, popTerms):
        for term in popTerms:
            self.popular_term_list.insert(END, term)

    def loadAffeceted(self, affectedOrgs):
        for org in affectedOrgs:
            self.affected_orgs_list.insert(END, org)

    def loadSentient(self, sentimentResult):
        self.sentiment_text.delete("1.0", END)
        self.sentiment_text.insert(END, sentimentResult)
