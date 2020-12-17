import tkinter as tk


# Constants
THEME_COLOR = "#375362"
q_font = ("Arial", 20)


# Classes
# todo: create quiz interface class
class QuizInterface(tk.Tk):
    """  """

    def __init__(self):
        """  """
        super().__init__()
        self.title("Quizzler")
        self.config(padx=20, pady=20, background=THEME_COLOR)
        self.init_UI()
        self.mainloop()

    def init_UI(self):
        self.score = Score(self)
        self.score.grid(row=0, column=1)

        self.q_card = QuestionCard(self)
        self.q_card.grid(row=1, column=0, columnspan=2)

        self.image_true = tk.PhotoImage(file="images/true.png")
        self.button_true = Button(self, image=self.image_true)
        self.button_true.grid(row=2, column=0)

        self.image_false = tk.PhotoImage(file="images/false.png")
        self.button_false = Button(self, image=self.image_false)
        self.button_false.grid(row=2, column=1)


class Score(tk.Label):
    """  """

    def __init__(self, parent, *args, **kwargs):
        """  """
        super().__init__(parent, *args, **kwargs)
        self.config(
            text=f"Score: 0",
            background=THEME_COLOR,
            foreground="white"
        )


class QuestionCard(tk.Canvas):
    """  """

    def __init__(self, parent, *args, **kwargs):
        """  """
        super().__init__(parent, *args, **kwargs)
        self.config(width=250, height=200, background="white")
        self.question = self.create_text(
            100, 100, text="Test Question", font=q_font, width=180)


class Button(tk.Button):
    """  """

    def __init__(self, parent, *args, **kwargs):
        """  """
        super().__init__(parent, *args, **kwargs)
        self.config(
            relief="flat",
            highlightthickness=0
        )
