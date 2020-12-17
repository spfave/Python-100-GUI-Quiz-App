import tkinter as tk
from quiz_brain import QuizBrain


# Constants
THEME_COLOR = "#375362"
q_font = ("Arial", 20, "italic")
s_font = ("Arial", 14, "bold")


# Classes
class QuizInterface(tk.Tk):
    """  """

    # use ':' after variable name to define variable type
    # for func/method can use '->'after func declaration to define variable return type
    def __init__(self, quiz_brain: QuizBrain):
        """  """
        self.quiz = quiz_brain
        self.timer = None

        super().__init__()
        self.title("Quizzler")
        self.config(padx=20, pady=20, background=THEME_COLOR)
        self.init_UI()
        self.get_next_question()

        self.mainloop()

    def init_UI(self):
        self.score = Score(self)
        self.score.grid(row=0, column=0, columnspan=2, pady=10)

        self.q_card = QuestionCard(self)
        self.q_card.grid(row=1, column=0, columnspan=2, pady=10)

        self._image_true = tk.PhotoImage(file="images/true.png")
        self.button_true = Button(
            self, image=self._image_true, command=self.click_true)
        self.button_true.grid(row=2, column=0, pady=10)

        self._image_false = tk.PhotoImage(file="images/false.png")
        self.button_false = Button(
            self, image=self._image_false, command=self.click_false)
        self.button_false.grid(row=2, column=1, pady=10)

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score.refresh(self.quiz.score)
            new_question = self.quiz.next_question()
            self.q_card.refresh(new_question)
        else:
            self.q_card.config(background="white")
            self.q_card.itemconfig(self.q_card.question,
                                   text="You've completed the quiz")
            self.button_true.disable()
            self.button_false.disable()

    def click_true(self):
        answer = self.quiz.check_answer("true")
        self.q_card.indicate_answer(answer)
        self.after(500, self.get_next_question)
        # self.get_next_question()

    def click_false(self):
        answer = self.quiz.check_answer("false")
        self.q_card.indicate_answer(answer)
        self.after(500, self.get_next_question)
        # self.get_next_question()


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

    def refresh(self, score):
        self.config(text=f"Score {score}")


class QuestionCard(tk.Canvas):
    """  """

    def __init__(self, parent, *args, **kwargs):
        """  """
        super().__init__(parent, *args, **kwargs)
        self.config(width=300, height=250, background="white")
        self.question = self.create_text(
            150, 125,
            text="Test Question", font=q_font, fill=THEME_COLOR,
            width=280,
        )

    def refresh(self, q_text):
        self.config(background="white")
        self.itemconfig(self.question, text=q_text)

    def indicate_answer(self, answer_right):
        if answer_right:
            self.config(background="green")
        else:
            self.config(background="red")


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

    def disable(self):
        self.config(state="disable")
