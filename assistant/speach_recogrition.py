from asyncio.windows_events import NULL
from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
import speech_recognition # распознавание пользовательской речи (Speech-To-Text)
import json  # работа с json-файлами и json-строками
import os  # работа с файловой системой

import pyaudio

import func.external.browser.internet # работа с интернет соединением

bot_speak = NULL
internet_is_up = False

internet_is_up = func.external.browser.internet.check_is_up()

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
# инициализация инструментов распознавания и ввода речи
recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()

with microphone:
    # регулирование уровня окружающего шума
    recognizer.adjust_for_ambient_noise(microphone, duration=2)

def recognize_voice(*args: tuple):
    print("ПРОСЛУШКА!")
    """
    Распознавание аудио
    """

    if(internet_is_up):
        with microphone:
            try:
                recognized_data = ""
                
                audio = recognizer.listen(microphone, 5, 5)

                # использование online-распознавания через Google
                recognized_data = recognizer.recognize_google(audio, language="ru").lower()
            except:
                print("Sorry")
    else:
        recognized_data = use_offline_recognition()
        for text in recognized_data:
            print(text)
    return recognized_data


def use_offline_recognition():
    """
    Переключение на оффлайн-распознавание речи
    :return: распознанная фраза
    """
    # проверка наличия модели на нужном языке в каталоге приложения
    if not os.path.exists("models/vosk-model-ru-0.22"):
        print("Please download the model from:\n"
            "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
        exit(1)

    model = Model("models/vosk-model-ru-0.22")
            
    offline_recognizer = KaldiRecognizer(model, 16000)
            
    p = pyaudio.PyAudio()
            
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1, 
        rate=16000, 
        input=True, 
        frames_per_buffer=8000
    )
            
    stream.start_stream()

    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (offline_recognizer.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(offline_recognizer.Result())
            if answer['text']:
                yield answer['text']