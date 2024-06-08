import openai
from GPT_API.config import gpt_header
import requests
from bs4 import BeautifulSoup

openai.api_key = gpt_header['GPT_KEY']


def info(doc):
    with open(doc, 'r') as f:
        inf = f.read()
        return inf


def user_question_func(message):
    """Функция выводит ответ Gpt"""
    response = openai.chat.completions.create(model="gpt-4o", messages=[
        {"role": "system", "content": "Ты эксперт по крипто бирже Латокен, отвечай на вопросы о Латокен,"
                                      "основываясь на предоставленных ссылках. Используй предоставленные ссылки и"
                                      "предоставленную дополнительную информацию,"
                                      "чтобы находить наиболее актуальную информацию о Latoken,"},
        {"role": "system", "content": "не формируй слишком длинные ответы, извлекай только наиболее важную информаицю,"
                                      "формируй краткие ответы"},
        {"role": "system", "content": "не давай лишнею информацию, только ту что в запросе"},
        {"role": "user", "content": f"{message}"},
        {"role": "user", "content": "Cсылка: https://deliver.latoken.com/about"},
        {"role": "user", "content": "Cсылка: https://deliver.latoken.com/hackathon"},
        {"role": "user", "content": f"Дополнительная информация: {info_1}"},
        {"role": "user", "content": f"Дополнительная информация: {info_2}"},
        {"role": "user", "content": f"Дополнительная информация: {info_3}"},
        {"role": "user", "content": f"Дополнительная информация: {info_4}"},
        {"role": "user", "content": f"Дополнительная информация: {info_5}"},
        {"role": "user", "content": f"Дополнительная информация: {info_6}"},
        {"role": "user", "content": f"Дополнительная информация: {info_7}"},
        {"role": "user", "content": f"Дополнительная информация: {info_0}"},
        {"role": "user", "content": f"Дополнительная информация: {task}"}
    ]
                                              )
    question = response.choices[0].message.content
    return question


info_0 = info('/home/zan/PycharmProjects/gpt_bot/GPT_API/s_info')
info_1 = info('/home/zan/PycharmProjects/gpt_bot/GPT_API/schedule')
info_2 = info('/home/zan/PycharmProjects/gpt_bot/GPT_API/s_info_2')
info_3 = info('/home/zan/PycharmProjects/gpt_bot/GPT_API/s_info_3')
info_4 = info('/home/zan/PycharmProjects/gpt_bot/GPT_API/s_info_4')
info_5 = info('/home/zan/PycharmProjects/gpt_bot/GPT_API/s_info_5')
info_6 = info('/home/zan/PycharmProjects/gpt_bot/GPT_API/s_info_6')
info_7 = info('/home/zan/PycharmProjects/gpt_bot/GPT_API/s_info_7')
task = info('/home/zan/PycharmProjects/gpt_bot/GPT_API/task')
