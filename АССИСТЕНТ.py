import sys
import os

import webbrowser
import pyperclip
import pyautogui as root
from time import sleep

import speech_recognition


# Цвета
WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'
VIOLET = '\033[35m'
YELLOW = '\033[33m'
BLUE = '\033[34m'


sr = speech_recognition.Recognizer()
# Вермя после которого фраза будет принята
sr.pause_threshold = 0.5

# Список фраз, которые нужно убрать перед анализом команд
phrases = {
    'name': ('name_your_assistant', ),
    'to_do': ('включи', 'покажи', 'открой')
}
# Список комманд
commands = {
    'find_in_browser': ('загугли', 'найди', 'узнай'),
    'search_video_on_youtube': 'видео',
    'listen_yandex_music': ('музыка', 'музыку'),
    'telegram': ('telegram', 'телеграм', 'телегу'),
    'end_the_program': ('выключайся', 'выключая', 'выключись')
}


def listen_command():
    """Функция возвращает полученное аудио в текст"""
    try:
        with speech_recognition.Microphone() as Mic:
            sr.adjust_for_ambient_noise(source=Mic)
            audio = sr.listen(source=Mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query

    except speech_recognition.UnknownValueError:
        return f'{VIOLET}Говорите громче и чётче, запрос не обработан...{WHITE}'


def find_in_browser(find):
    """Функция ищет информацию в интернете"""
    webbrowser.open_new(f'https://www.google.com/search?q={find}')


def search_video_on_youtube(find):
    """Функция ищет видео на ютубе"""
    webbrowser.open_new(f'https://www.youtube.com/results?search_query={find}')


def listen_yandex_music(smthn):
    """Функуия запуска Яндекс музыки"""
    webbrowser.open_new('your_path')
    sleep(2)
    # Ищем иконку ЯМ на главной странице
    a = root.locateCenterOnScreen('YM.png', confidence=0.9)
    root.moveTo(a)
    root.click()
    sleep(4)
    # Ищем 'мою волну' на странице ЯМ
    a = root.locateCenterOnScreen('My_Wave.png', confidence=0.8)
    root.moveTo(a)
    root.click()


def telegram(smthn):
    """Функцция запускает телеграм"""
    os.startfile('your_path')


def end_the_program(smthn):
    """Функуия завершает работу программы"""
    sys.exit()


def main():
    while True:
        query = listen_command()
        print(query)

        # Удаляем слова, не нужные для анализа
        for phrase in phrases:
            for word in phrases[phrase]:
                query = query.replace(word, '').strip()

        # Разделяем запрос на команду и доп уточнения для команды
        voice_query = query.strip().split(' ')
        command = voice_query[0]
        command_options = ' '.join(voice_query[1::])

        for key in commands.keys():
            if command in commands.get(key):
                globals()[key](command_options)


if __name__ == '__main__':
    main()
