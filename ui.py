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
        self.config(padx=50, pady=50, background=THEME_COLOR)
        self.init_UI()
        self.mainloop()

    def init_UI(self):
        self.q_card = QuestionCard(self)
        self.q_card.grid(row=1, column=0, columnspan=2)


# todo: create question card class
class QuestionCard(tk.Canvas):
    """  """

    def __init__(self, parent):
        """  """
        super().__init__(parent)
        self.config(width=200, height=200, background="white")
        self.question = self.create_text(100, 100, text="Test Question")


# todo: create button class
class Button():
    """  """

    def __init__(self):
        """  """
        pass
