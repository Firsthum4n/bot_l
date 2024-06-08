from bot.core import bot
from GPT_API.open_ai_handler import user_question_func


class MyBot:
    """Класс обертка для Телеграмм Бот"""
    def __init__(self) -> None:
        """Конструктор"""
        MyBot.init_commands()
        bot.infinity_polling()

    @staticmethod
    def init_commands() -> None:
        """ Инициализация команд
        :return: None
        """

        @bot.message_handler(commands=['start', 'hello'])
        def start(message):
            """Функция приветствия, выводит на экран приветствие"""
            bot.send_message(message.chat.id, text="Привет, {0.first_name}!👋"
                                                   "Рад видеть тебя здесь. Приглашаю тебя зарегистрироваться на наш "
                                                   "хакатон,"
                                                   "который стартует каждую пятницу в 18:00 по московскому времени. "
                                                   "Это отличная возможность показать свои навыки и получить "
                                                   "предложение о работе."
                                                   "Регистрируйся по ссылке: https://t.me/gpt_web3_hackathon/6694 "
                                                   "Если у тебя есть вопросы, не стесняйся задавать!".format(
                message.from_user))


        @bot.message_handler(content_types=['text'])
        def main(message: str) -> None:
            bot.send_message(message.chat.id, '{}'.format(user_question_func(message)))


