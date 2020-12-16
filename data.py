import requests


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


# Main
question_data = generate_quiz_questions()
