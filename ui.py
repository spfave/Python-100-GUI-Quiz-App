import tkinter as tk


# Constants
THEME_COLOR = "#375362"


# Classes
# todo: create quiz interface class
class QuizInterface(tk.Tk):
    """  """

    def __init__(self):
        """  """
        super().__init__()
        self.title("Quizzler")
        self.config(padx=25, pady=50, background=THEME_COLOR)
        self.init_UI()
        self.mainloop()

    def init_UI(self):
        self.score = Score(self)
        self.score.grid(row=0, column=1)
        self.q_card = QuestionCard(self)
        self.q_card.grid(row=1, column=0, columnspan=2)


class Score(tk.Label):
    """  """

    def __init__(self, parent):
        """  """
        super().__init__(parent)
        self.config(text=f"Score: 0")


class QuestionCard(tk.Canvas):
    """  """

    def __init__(self, parent):
        """  """
        super().__init__(parent)
        self.config(width=200, height=200, background="white")
        self.question = self.create_text(
            100, 100, text="Test Question", width=180)


# todo: create button class
class Button():
    """  """

    def __init__(self):
        """  """
        pass
