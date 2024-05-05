import cv2
import Main
import Service

@Main.bot.message_handler(commands=['start'])
def start_command(message):
    Main.bot.send_message(message.chat.id, "Сфотографируйте QR код на устройстве")
    img = cv2.imread('img1.jpg')
    detect = cv2.QRCodeDetector()
    result = detect.detectAndDecode(img)
    print(result)


@Main.bot.message_handler(content_types=['photo'])
def handle_photo(message):
    service = Service.Service()
    service.decoder(message)


# Не забудьте запустить бота
Main.bot.polling(none_stop=True)