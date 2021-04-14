# Import tkinter and agent.py
from tkinter import *
from agent import *
from wikipedia_api import *
from twitter_api import *

# botname specified
bot_name = "Steven"

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        self.agent = Agent()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chatbot")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=600, height=550, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=30, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=0, pady=0)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(state=NORMAL)

        intro_msg = "Welcome, we are here to help you with your computer issues. Please type \"Hello\" or the type " \
                    "of issue you are having, to begin. Please the keyword you want search and use the 'Search' button." \
                    " Please the type keyword and use the 'Tweet' button to print latest tweet on keyword. \n\n"
        self.text_widget.insert(END, intro_msg)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        # search  button
        search_button = Button(bottom_label, text="Search", font=FONT_BOLD, width=10, bg=BG_GRAY,
                                command=lambda: self._on_enter_search_wiki(None))
        search_button.place(relx=0.77, rely=0.08, relheight=0.03, relwidth=0.11)

        # search  button
        search_button = Button(bottom_label, text="Tweets", font=FONT_BOLD, width=10, bg=BG_GRAY,
                               command=lambda: self._on_enter_find_tweet(None))
        search_button.place(relx=0.88, rely=0.08, relheight=0.03, relwidth=0.11)

    # on enter pressed function defined
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return  # if there is no text entered
        msg = self.agent.spellCheck(msg)
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        intentions = self.agent.predictResponse(msg)
        msg2 = f"{bot_name}: {self.agent.getResponse(intentions)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

    # on enter search wikipedia
    def _on_enter_search_wiki(self, event):
        msg = self.msg_entry.get()
        self._insert_wiki_keyword(msg, "You")

    def _insert_wiki_keyword(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        botResponse = search_wiki(msg)
        msg2 = f"{bot_name}: {botResponse}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

    # on enter find tweet
    def _on_enter_find_tweet(self, event):
        msg = self.msg_entry.get()
        self._insert_twitter_keyword(msg, "You")

    def _insert_twitter_keyword(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        botResponse = get_tweets(msg)
        msg2 = f"{bot_name}: {botResponse}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
