import os  # работа с файловой системой
from gtts import gTTS # преобразование текста в речь
import playsound # проигрывание музыки


path = "./assistant/voice/"

file_voice_listen = path+"listen.mp3"
file_voice_nothingsay = path+"nothingsay.mp3"
file_voice_command_not_found = path+"command_not_found.mp3"
new_voice_path = ""

list_of_voices = {
    file_voice_listen: "слушаю",
    file_voice_nothingsay: "вы ничего не сказали",
    file_voice_command_not_found: "команда не найдена"
}

hello = False

for voice_path in list_of_voices.keys():
    if not os.path.exists(voice_path):
        voice = gTTS(list_of_voices[voice_path], lang="ru")
        voice.save(voice_path)
            
def gen_new_speech(*args: tuple):
    global new_voice_path
    
    new_voice_path = path+"new_voice.mp3"
    
    if not os.path.exists(new_voice_path):
        voice = gTTS(str(args), lang="ru")
        voice.save(new_voice_path)
        

def listen(*args: list):
    global hello
    hello = True
    playsound.playsound(file_voice_listen)

def nothingsay(*args: list):
    playsound.playsound(file_voice_nothingsay)
    
def command_not_found(*args: list):
    playsound.playsound(file_voice_command_not_found)
    
def new_voice_tell(*args: list):
    playsound.playsound(new_voice_path)
    if os.path.exists(new_voice_path):
        os.remove(new_voice_path)