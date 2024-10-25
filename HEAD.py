import telebot
from telebot import types
import threading  # Для блокировок
import json
import os
from upload_channel1 import upload_video_channel1
import shutil
from get_video_info_1 import get_titles_1, get_titles_2, get_titles_3, get_titles_4, get_titles_5, get_titles_6
import subprocess
import yadisk

# Функция для удаления папки на Яндекс Диске
def delete_folder_on_yandex_disk(folder_path):
    try:
        # Инициализация с использованием токена
        token_file = r'C:\Users\Даниил\Desktop\10k\yandex\tokenDanya.txt'
        with open(token_file, 'r') as f:
            yandex_token = f.read().strip()
        
        y = yadisk.YaDisk(token=yandex_token)
        
        # Удаление папки на Яндекс Диске
        if y.exists(folder_path):
            y.remove(folder_path, permanently=True)
            print(f"Папка {folder_path} успешно удалена.")
        else:
            print(f"Папка {folder_path} не найдена на Яндекс Диске.")
    except Exception as e:
        print(f"Ошибка при удалении папки {folder_path}: {e}")

# Функция для проверки наличия минимум 4 файлов в папке
def check_stock_folder():
    stock_folder = r'C:\Users\Даниил\Desktop\M-parts\stock'
    # Получаем список всех файлов в папке
    files = [f for f in os.listdir(stock_folder) if os.path.isfile(os.path.join(stock_folder, f))]
    
    # Проверяем, есть ли как минимум 4 файла
    return len(files) >= 4

# Путь до скриптов
yandex_script = r'C:\Users\Даниил\Desktop\10k\yandex\yandex.py'
yandex_script_2 = r'C:\Users\Даниил\Desktop\10k\yandex\yandex2.py'
yandex_script_3 = r'C:\Users\Даниил\Desktop\10k\yandex\yandex3.py'
yandex_script_4 = r'C:\Users\Даниил\Desktop\10k\yandex\yandex4.py'
yandex_script_5 = r'C:\Users\Даниил\Desktop\10k\yandex\yandex5.py'
yandex_script_6 = r'C:\Users\Даниил\Desktop\10k\yandex\yandex6.py'

adobe_script = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere.py'
adobe_script2 = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere2.py'
adobe_script3 = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere3.py'
adobe_script4 = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere4.py'
adobe_script5 = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere5.py'
adobe_script6 = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere6.py'

italy = "►Questo è un canale con notizie indipendenti e analisi degli eventi attuali. Qui condivido un punto di vista non convenzionale sulla realtà e esprimo la mia opinione. Il video è un commento formato dalla mia opinione personale."
espanol = "► Este es un canal con noticias independientes y análisis de los eventos actuales. Aquí comparto un punto de vista no convencional sobre la realidad y expreso mi opinión. El video es un comentario formado por mi opinión personal."

# Функция для запуска Python скрипта
def run_python_script(script_path):
    try:
        # Запуск скрипта
        subprocess.run(['python', script_path], check=True)
        print(f"Скрипт {script_path} выполнен успешно.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении скрипта {script_path}: {e}")

# Загружаем конфигурацию из файла config.json
# with open("config2.json", "r") as config_file:
#     config = json.load(config_file)
# with open("config2.json", "r") as config_file:
#     config2 = json.load(config_file)
# with open("config3.json", "r") as config_file:
#     config3 = json.load(config_file)
# with open("config4.json", "r") as config_file:
#     config4 = json.load(config_file)
# with open("config5.json", "r") as config_file:
#     config5 = json.load(config_file)
# with open("config6.json", "r") as config_file:
#     config6 = json.load(config_file)

# Читаем параметры из конфигурации
# telegram_token = config['telegram_token']

# client_secret_file = config['client_secret_file']

# client_secret_file2 = config2['client_secret_file']

# client_secret_file3 = config3['client_secret_file']

# client_secret_file4 = config4['client_secret_file']

# client_secret_file5 = config5['client_secret_file']

# client_secret_file6 = config6['client_secret_file']

telegram_token = "7404505828:AAFfk1N49GpVMsN2x_kuMUp0nvV-GdLvihw"

client_secret_file = "sekretiki.json"

client_secret_file2 = "sekretiki2.json"

client_secret_file3 = "sekretiki3.json"

client_secret_file4 = "sekretiki4.json"

client_secret_file5 = "sekretiki5.json"

client_secret_file6 = "sekretiki6.json"

# Путь к файлам токенов для двух каналов
USER_TOKENS = {
    "Канал 1": "channel1_token.json",  # для кнопок 1 2
    "Канал 2": "channel2_token.json", # для кнопок 3 4
    "Канал 3": "channel3_token.json",  # для кнопок 5 6
    "Канал 11": "channel1_token.json",  # для кнопок 1 2
    "Канал 22": "channel2_token.json", # для кнопок 3 4
    "Канал 33": "channel3_token.json",  # для кнопок 5 6
}

# Путь к видео и превью
VIDEO_FOLDER_1 = "video_channel_1/"
PREVIEW_FOLDER_1 = "preview_channel_1/"
VIDEO_FOLDER_2 = "video_channel_2/"
PREVIEW_FOLDER_2 = "preview_channel_2/"
VIDEO_FOLDER_3 = "video_channel_3/"
PREVIEW_FOLDER_3 = "preview_channel_3/"
VIDEO_FOLDER_4 = "video_channel_4/"
PREVIEW_FOLDER_4 = "preview_channel_4/"
VIDEO_FOLDER_5 = "video_channel_5/"
PREVIEW_FOLDER_5 = "preview_channel_5/"
VIDEO_FOLDER_6 = "video_channel_6/"
PREVIEW_FOLDER_6 = "preview_channel_6/"

# Создаем блокировку
lock = threading.Lock()

# Токен вашего бота
bot = telebot.TeleBot(telegram_token)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button1 = types.KeyboardButton("Италия 1")  # Канал 1
    button2 = types.KeyboardButton("Италия 2")  # Канал 1
    button3 = types.KeyboardButton("Испания 3") # Канал 2
    button4 = types.KeyboardButton("Испания 4") # Канал 2
    button5 = types.KeyboardButton("Италия 5") # Канал 3
    button6 = types.KeyboardButton("Италия 6") # Канал 3
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id, "Выберите канал для загрузки видео:", reply_markup=markup)
    
def get_tags_from_file(tags_file):
    with open(tags_file, 'r', encoding='utf-8') as f:
        tags = f.read().strip().split(',')  # Читает и разделяет теги по запятой
    return [tag.strip() for tag in tags]  # Убирает лишние пробелы у каждого тега


# Функция для обработки загрузки всех 4 видео
def handle_upload_all_videos(message, channel, video_folder, preview_folder, titles, descriptions, token_file):
    if lock.locked():
        bot.send_message(message.chat.id, "Подождите, пока завершится текущая загрузка.")
        return

    with lock:
        try:
            bot.send_message(message.chat.id, "Начинаю загрузку видео...")
            for i in range(1, 5):
                video_file = os.path.join(video_folder, f"{i}.mp4")
                thumbnail_file = os.path.join(preview_folder, f"{i}.jpg")
                title = titles[i-1]
                description = descriptions[i-1]
                tags12 = get_tags_from_file(r'C:\Users\Даниил\Desktop\10k\youtube\tags12.txt')  # Получаем теги из файла
                tags34 = get_tags_from_file(r'C:\Users\Даниил\Desktop\10k\youtube\tags34.txt')
                tags56 = get_tags_from_file(r'C:\Users\Даниил\Desktop\10k\youtube\tags56.txt')
                category_id = "25"  # Категория видео

                # Логика загрузки видео на канал
                if channel == "Канал 1":
                    video_id = upload_video_channel1(video_file, thumbnail_file, title, description, category_id, client_secret_file, token_file, tags12)
                elif channel == "Канал 2":
                    video_id = upload_video_channel1(video_file, thumbnail_file, title, description, category_id, client_secret_file2, token_file, tags34)
                elif channel == "Канал 3":
                    video_id = upload_video_channel1(video_file, thumbnail_file, title, description, category_id, client_secret_file3, token_file, tags56)
                elif channel == "Канал 11":
                    video_id = upload_video_channel1(video_file, thumbnail_file, title, description, category_id, client_secret_file4, token_file, tags12)
                elif channel == "Канал 22":
                    video_id = upload_video_channel1(video_file, thumbnail_file, title, description, category_id, client_secret_file5, token_file, tags34)
                elif channel == "Канал 33":
                    video_id = upload_video_channel1(video_file, thumbnail_file, title, description, category_id, client_secret_file6, token_file, tags56)

                if video_id:
                    bot.send_message(message.chat.id, f"Видео {i} успешно загружено! ID видео: {video_id}")
                else:
                    bot.send_message(message.chat.id, f"Ошибка при загрузке видео {i}.")
        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка: {str(e)}")

# Обработчик нажатий на кнопки
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    
    # Проверка наличия файлов в папке
    if not check_stock_folder():
        bot.send_message(message.chat.id, "В папке кончились стоки. Пожалуйста, добавьте файлы.")
        return  # Прекращаем выполнение, если файлов недостаточно
    
    if message.text in ["Италия 1"]:

        
        video_folder = VIDEO_FOLDER_1
        preview_folder = PREVIEW_FOLDER_1

        # Вызов скрипта yandex.py
        script_path = r'C:/Users/Даниил/Desktop/10k/yandex/yandex.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")

        titles = get_titles_1()
        descriptions = [f"{titles[0]}\n{italy}",f"{titles[1]}\n{italy}",f"{titles[2]}\n{italy}",f"{titles[3]}\n{italy}"]
        # #Вызов скрипта RunPremiere.py
        script_path = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")


        # Загружаем все 4 видео на Канал 1
        handle_upload_all_videos(message, "Канал 1", video_folder, preview_folder, titles, descriptions, USER_TOKENS["Канал 1"])
        # Удаление папки на Яндекс Диске для 1 кнопки
        delete_folder_on_yandex_disk("/newscontent/1")

        
    elif message.text in ["Италия 2"]:
        

        video_folder = VIDEO_FOLDER_1
        preview_folder = PREVIEW_FOLDER_1

        # Вызов скрипта yandex.py
        script_path = r'C:/Users/Даниил/Desktop/10k/yandex/yandex2.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")

        titles = get_titles_2()
        descriptions = [f"{titles[0]}\n{italy}",f"{titles[1]}\n{italy}",f"{titles[2]}\n{italy}",f"{titles[3]}\n{italy}"]
        # Вызов скрипта RunPremiere.py
        script_path = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere2.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")


        # Загружаем все 4 видео на Канал 1
        handle_upload_all_videos(message, "Канал 11", video_folder, preview_folder, titles, descriptions, USER_TOKENS["Канал 1"])
# Удаление папки на Яндекс Диске для 1 кнопки
        delete_folder_on_yandex_disk("/newscontent/2")

    elif message.text in ["Испания 3"]:
        

        video_folder = VIDEO_FOLDER_2
        preview_folder = PREVIEW_FOLDER_2

        # Вызов скрипта yandex.py
        script_path = r'C:/Users/Даниил/Desktop/10k/yandex/yandex3.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")
        titles = get_titles_3()
        descriptions = [f"{titles[0]}\n{espanol}",f"{titles[1]}\n{espanol}",f"{titles[2]}\n{espanol}",f"{titles[3]}\n{espanol}"]
        # Вызов скрипта RunPremiere.py
        script_path = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere3.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")


        # Загружаем все 4 видео на Канал 1
        handle_upload_all_videos(message, "Канал 2", video_folder, preview_folder, titles, descriptions, USER_TOKENS["Канал 2"]) 
# Удаление папки на Яндекс Диске для 1 кнопки
        delete_folder_on_yandex_disk("/newscontent/3")
              
    elif message.text in ["Испания 4"]:
        

        video_folder = VIDEO_FOLDER_2
        preview_folder = PREVIEW_FOLDER_2

        # Вызов скрипта yandex.py
        script_path = r'C:/Users/Даниил/Desktop/10k/yandex/yandex4.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")

        titles = get_titles_4()
        descriptions = [f"{titles[0]}\n{espanol}",f"{titles[1]}\n{espanol}",f"{titles[2]}\n{espanol}",f"{titles[3]}\n{espanol}"]
        # Вызов скрипта RunPremiere.py
        script_path = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere4.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")


        # Загружаем все 4 видео на Канал 1
        handle_upload_all_videos(message, "Канал 22", video_folder, preview_folder, titles, descriptions, USER_TOKENS["Канал 2"])   
# Удаление папки на Яндекс Диске для 1 кнопки
        delete_folder_on_yandex_disk("/newscontent/4")
        
    elif message.text in ["Италия 5"]:
        

        video_folder = VIDEO_FOLDER_1
        preview_folder = PREVIEW_FOLDER_1

        # Вызов скрипта yandex.py
        script_path = r'C:/Users/Даниил/Desktop/10k/yandex/yandex5.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")

        titles = get_titles_5()
        descriptions = [f"{titles[0]}\n{italy}",f"{titles[1]}\n{italy}",f"{titles[2]}\n{italy}",f"{titles[3]}\n{italy}"]
        # #Вызов скрипта RunPremiere.py
        script_path = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere5.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")


        # Загружаем все 4 видео на Канал 1
        handle_upload_all_videos(message, "Канал 3", video_folder, preview_folder, titles, descriptions, USER_TOKENS["Канал 3"])
# Удаление папки на Яндекс Диске для 1 кнопки
        delete_folder_on_yandex_disk("/newscontent/5")
        
    elif message.text in ["Италия 6"]:
        

        video_folder = VIDEO_FOLDER_1
        preview_folder = PREVIEW_FOLDER_1

        # Вызов скрипта yandex.py
        script_path = r'C:/Users/Даниил/Desktop/10k/yandex/yandex6.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")

        titles = get_titles_6()
        descriptions = [f"{titles[0]}\n{italy}",f"{titles[1]}\n{italy}",f"{titles[2]}\n{italy}",f"{titles[3]}\n{italy}"]
        # Вызов скрипта RunPremiere.py
        script_path = r'C:\Users\Даниил\Desktop\10k\adobe\RunPremiere6.py'
        script_dir = os.path.dirname(script_path)

        try:
            result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True, cwd=script_dir)
            print(f"Скрипт {script_path} выполнен успешно.")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта {script_path}: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Сообщение об ошибке: {e.stderr}")


        # Загружаем все 4 видео на Канал 1
        handle_upload_all_videos(message, "Канал 33", video_folder, preview_folder, titles, descriptions, USER_TOKENS["Канал 3"])
 # Удаление папки на Яндекс Диске для 1 кнопки
        delete_folder_on_yandex_disk("/newscontent/6")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите одну из доступных кнопок.")  

bot.polling(none_stop=True)
