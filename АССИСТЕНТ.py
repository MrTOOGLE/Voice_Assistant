import sys
import os

import webbrowser
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
# Список комманд
commands = {
    'find_in_browser': ('загугли', 'найди', 'узнай'),
    'listen_yandex_music': ('включи музыку', 'вруби музыку', 'врубая музыку'),
    'telegram': ('запусти telegram', 'открой telegram', 'запусти телегу', 'открой телегу'),
    'end_the_program': ('выключайся', 'завершая работу', 'завершай работу')
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
    webbrowser.open_new(f'https://www.google.com/search?q={" ".join(find.split())}')


def listen_yandex_music():
    """Функуия включения Яндекс музыки (иностранный рэп и хип-хоп)"""
    """❗❗ Возможна замена порядка расположения кнопки запуске ❗❗"""
    webbrowser.open_new('https://music.yandex.ru/radio')
    root.moveTo(505, 555, 3)
    root.click()


def telegram():
    """Функцция запускает телеграм"""
    os.startfile('your path')


def end_the_program():
    """Функуия завершает работу программы"""
    sys.exit()


def main():
    while True:
        query = listen_command()
        print(query)

        command = ''
        # Если запрос на поиск информации в интернете, то убираем из запроса слова из команды 'open_browser'
        # Иначе если один из вариантов вызова комманды подходит, то записываем в переменную название команды
        if query.startswith(commands['find_in_browser']):
            for_browser = query
            command = 'find_in_browser'
            for name_command in commands['find_in_browser']:
                for_browser = for_browser.replace(name_command, '').strip()
        else:
            for name_commands, version_names_commad in commands.items():
                if query in version_names_commad:
                    command = name_commands

        if command != '' and command != 'find_in_browser':
            # Вызываем функцию по ключу команды, если в ней нет лишних фраз
            """
            Было раньше так:
            if command == 'clear_task':
                clear_task()
            Теперь:
                globals()[command(='clear_task')]() == clear_task()
            """
            globals()[command]()
        elif command == 'find_in_browser':
            find_in_browser(for_browser)


if __name__ == '__main__':
    main()
