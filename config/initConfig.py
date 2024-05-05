import yaml
import telebot

class InitConfig:
    def init(self):
        # Открываем файл 'app.yml' и читаем его содержимое
        with open('app.yml', 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        bot = telebot.TeleBot(data_loaded['api']['TOKEN'])

        def run_bot():
            bot.polling(none_stop=True)