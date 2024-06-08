import openai
from SITE_API.config import gpt_header

openai.api_key = gpt_header['GPT_KEY']


def user_question_func(message):
    """Функция выводит ответ Gpt"""
    response = openai.chat.completions.create(model="gpt-4o", messages=[
        {"role": "system", "content": "Ты эксперт по крипто бирже Латокен, отвечай на вопросы о Латокен,"
                                      "основываясь на предоставленных ссылках. Используй предоставленные ссылки, "
                                      "чтобы находить наиболее актуальную информацию о Latoken"},
        {"role": "user", "content": f"{message}"},
        {"role": "user", "content": "Cсылка: deliver.latoken.com/about"},
        {"role": "user", "content": "Cсылка: deliver.latoken.com/hackathon"},
    ]
                                              )
    question = response.choices[0].message.content
    return question
