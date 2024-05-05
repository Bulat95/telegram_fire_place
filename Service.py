import cv2
import Main
import json
import telebot


class Service:
    def decoder(message):
        photo = message.photo[-1]
        # Получаем информацию о файле
        file_info = Main.bot.get_file(photo.file_id)
        downloaded_file = Main.bot.download_file(file_info.file_path)

        # Здесь вам нужно сохранить файл локально,
        # потому что cv2.imread() работает с локальными файлами
        save_path = 'photo.jpg'
        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Теперь вы можете считывать изображение из файла
        img = cv2.imread(save_path)

        detect = cv2.QRCodeDetector()
        result, _, _ = detect.detectAndDecode(img)  # получаем результат декодирования

        if result:  # проверяем, был ли декодирован QR-код
            Main.bot.reply_to(message, result)
        else:
            print("QR код не найден")
            Main.bot.reply_to(message, "QR код не найден")

    def readJson(self):
        filename = 'uuids.json'
        with open(filename, 'r') as file:
            data = json.load(file)
        login_uuid_dict = {uuid: "empty" for uuid in data["uuids"]}