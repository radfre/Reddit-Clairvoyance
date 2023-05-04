import tkinter as tk


class GUI:
    def __init__(self):
        # Create window
        self.window = tk.Tk()
        self.window.title('Reddit Top Posts')
        self.window.geometry('2000x500')
        self.window.configure(bg='gray')

        # Create label to display results

        self.frame1 = tk.Frame(self.window, relief=tk.GROOVE, bd=7)

        self.Title_label = tk.Label(self.frame1, text='', justify='left')
        self.Top_label = tk.Label(self.frame1, text='', font=('Arial', 8), justify='left')
        self.Users_label = tk.Label(self.frame1, text='', justify='left')

        self.Title_label.pack(side=tk.TOP, pady=10)
        self.Top_label.pack(side=tk.TOP, padx=20)
        self.Users_label.pack(side=tk.BOTTOM, padx=10, pady=5)

        self.frame1.pack(side=tk.LEFT)

    def loading(self):
        print('loading')

    def display_top_posts(self, top_posts_text):
        self.Top_label.config(text=top_posts_text)
        self.window.mainloop()
