from bot.core import bot
from Keyboards.core import markup, hello_markup, menu_markup
from SITE_API.site_heandlears_hotel_search import hotel_values_func, get_hotel_response_custom
from DATABASE.core import write_user, get_name, hihgt_low, return_reqs, update




class MyBot:
    """Класс обертка для Телеграмм Бот"""
    def __init__(self) -> None:
        """Конструктор"""
        MyBot.init_commands()  # инициализация команд
        bot.infinity_polling()  # запуск обработки в цикле

    @staticmethod
    def init_commands() -> None:
        """ Инициализация команд
        :return: None

        """

        @bot.message_handler(commands=['start', 'hello'])
        def start(message):
            """Функция приветствия, выводит на экран приветствие"""
            write_user(message)
            bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот".format(
                message.from_user), reply_markup=hello_markup)

        @bot.message_handler(content_types=['text'])
        def main_menu(message: str) -> None:
            """Функция выводящая на экран меню"""
            write_user(message)
            if message.text == 'привет👋' or message.text == 'меню' or message.text == '◀️ Меню':
                bot.send_message(message.chat.id, text="Это главное меню. Выбери один из пунктов",
                                 reply_markup=markup)
                bot.register_next_step_handler(message, get_first_cur)

        def get_first_cur(message: str) -> None:
            """Функция меню, выводит команды меню"""
            write_user(message)
            if message.text == '/low':
                bot.send_message(message.chat.id, 'Название отеля?', reply_markup=menu_markup)
                hihgt_low('1')
                bot.register_next_step_handler(message, hotel_search_1)
            if message.text == '/high':
                bot.send_message(message.chat.id, 'Название отеля?', reply_markup=menu_markup)
                hihgt_low('2')
                bot.register_next_step_handler(message, hotel_search_1)
            if message.text == '/custom':
                bot.send_message(message.chat.id, 'Название отеля?', reply_markup=menu_markup)
                bot.register_next_step_handler(message, hotel_search_c1)
            if message.text == '/history':
                bot.send_message(message.chat.id, '{}'.format(return_reqs()), reply_markup=menu_markup)

        def hotel_search_1(message: str) -> None:
            """Функция отеля, получает параметр названия отеля"""
            write_user(message)
            update(message, 'hotel_name')
            bot.send_message(message.chat.id, 'Сколько отелей показать? ', reply_markup=menu_markup)
            bot.register_next_step_handler(message, hotel_search_2)

        def hotel_search_2(message: str) -> None:
            """Функция отеля, выводит в чат результат поиска по параметрам"""
            write_user(message)
            quantity = message.text
            name = get_name('hotel_name')
            sort = get_name('hight_or_low')
            bot.send_message(message.chat.id, '{}'.format(hotel_values_func(name, int(sort), quantity)),
                             reply_markup=menu_markup)

        def hotel_search_c1(message: str) -> None:
            """Функция отеля custom, получает параметр названия отеля"""
            write_user(message)
            update(message, 'hotel_name')
            bot.send_message(message.chat.id, 'Дата заезда(формат-"2024-02-14"): ', reply_markup=menu_markup)
            bot.register_next_step_handler(message, hotel_search_c2)

        def hotel_search_c2(message: str) -> None:
            """Функция отеля custom, получает параметр даты заезда"""
            write_user(message)
            update(message, 'arrival_date')
            bot.send_message(message.chat.id, 'дата выезда(формат-"2024-02-14"): ', reply_markup=menu_markup)
            bot.register_next_step_handler(message, hotel_search_c3)

        def hotel_search_c3(message: str) -> None:
            """Функция отеля custom, получает параметр даты выезда"""
            write_user(message)
            update(message, 'departure_date')
            bot.send_message(message.chat.id, 'Сколько отелей показать ? ', reply_markup=menu_markup)
            bot.register_next_step_handler(message, hotel_search_c4)

        def hotel_search_c4(message: str) -> None:
            """Функция отеля custom, выводит в чат результат поиска по параметрам"""
            write_user(message)
            quantity = message.text
            name = get_name('hotel_name')
            date1 = get_name('arrival_date')
            date2 = get_name('departure_date')
            bot.send_message(message.chat.id, '{}'.format(get_hotel_response_custom(name, quantity, date1, date2)),
                             reply_markup=menu_markup)





