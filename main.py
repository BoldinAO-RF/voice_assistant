import assistant.speach_recogrition as speach_recogrition
import commands.command_executor as command_executor
from termcolor import colored

# подготовка корпуса для распознавания запросов пользователя с некоторой вероятностью
# (поиск похожих)
command_executor.prepare_corpus()

if __name__ == "__main__":
    while True:
        # старт записи речи с последующим выводом распознанной речи
        # и удалением записанного в микрофон аудио
        voice_input = speach_recogrition.recognize_voice()
        
        print(colored(voice_input, "blue"))
        
        command_executor.exec(voice_input)