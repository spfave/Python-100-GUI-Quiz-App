from quiz_brain import QuizBrain
from question_model import Question
from data import question_bank
import ui


# Main
quiz = QuizBrain(question_bank)
quiz_app = ui.QuizInterface(quiz)
