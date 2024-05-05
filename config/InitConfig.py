import yaml
import telebot


class InitConfig:
    def init(self):
        with open('app.yml', 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        bot = telebot.TeleBot(data_loaded['api']['TOKEN'])

        def run_bot():
            bot.polling(none_stop=True)
