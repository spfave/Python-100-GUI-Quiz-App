import tkinter as tk
from quiz_brain import QuizBrain


# Constants
THEME_COLOR = "#375362"
q_font = ("Arial", 20)
s_font = ("Arial", 14, "bold")


# Classes
class QuizInterface(tk.Tk):
    """  """

    def __init__(self, quiz_brain: QuizBrain):
        """  """
        self.quiz = quiz_brain

        super().__init__()
        self.title("Quizzler")
        self.config(padx=20, pady=20, background=THEME_COLOR)
        self.init_UI()
        self.mainloop()

    def init_UI(self):
        self.score = Score(self)
        self.score.grid(row=0, column=0, columnspan=2, pady=10)

        self.q_card = QuestionCard(self)
        self.q_card.grid(row=1, column=0, columnspan=2, pady=10)

        self._image_true = tk.PhotoImage(file="images/true.png")
        self.button_true = Button(self, image=self._image_true)
        self.button_true.grid(row=2, column=0, pady=10)

        self._image_false = tk.PhotoImage(file="images/false.png")
        self.button_false = Button(self, image=self._image_false)
        self.button_false.grid(row=2, column=1, pady=10)

    def get_next_question(self):
        new_question = self.quiz.next_question()
        self.q_card.refresh(new_question)


class Score(tk.Label):
    """  """

    def __init__(self, parent, *args, **kwargs):
        """  """
        super().__init__(parent, *args, **kwargs)
        self.config(
            text=f"Score: 0",
            font=s_font,
            background=THEME_COLOR,
            foreground="white",
        )


class QuestionCard(tk.Canvas):
    """  """

    def __init__(self, parent, *args, **kwargs):
        """  """
        super().__init__(parent, *args, **kwargs)
        self.config(width=300, height=250, background="white")
        self.question = self.create_text(
            150, 125,
            text="Test Question", font=q_font, fill=THEME_COLOR,
            width=180,
        )

    def refresh(self, q_text):
        self.itemconfig(self.question, text=q_text)
        pass


class Button(tk.Button):
    """  """

    def __init__(self, parent, *args, **kwargs):
        """  """
        super().__init__(parent, *args, **kwargs)
        self.config(
            relief="flat",
            bd=1,
            highlightthickness=0,
        )
