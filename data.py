import requests
from question_model import Question


# Functions
def generate_quiz_questions(num_questions=10, question_type="boolean"):
    """  """
    api_open_trivia = "https://opentdb.com/api.php"
    parameters = {
        "amount": num_questions,
        "type": question_type,
    }

    response = requests.get(url=api_open_trivia, params=parameters)
    response.raise_for_status()
    question_data = response.json()["results"]

    return question_data


def qdata_list_to_qobj_list(question_data):
    question_bank = []

    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    return question_bank


# Main
question_data = generate_quiz_questions()
question_bank = qdata_list_to_qobj_list(question_data)
