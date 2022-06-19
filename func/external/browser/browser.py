import webbrowser
from pyowm import OWM
import assistant.assistant_speeching as bs

def search_for_google(*args: tuple):
    if not args[0]: return
    search_term = " ".join(args[0])
    url_google_search = "https://www.google.com/search?q="+search_term
    webbrowser.open(url_google_search, new=0, autoraise=True)

def search_for_video_on_youtube(*args: tuple):
    """
    Поиск видео на YouTube с автоматическим открытием ссылки на список результатов
    :param args: фраза поискового запроса
    """
    if not args[0]: return
    search_term = " ".join(args[0])
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)
    
def weather(*args: tuple):
    owm = OWM('51c36b1c38b06959eb863e7cb29844f7')
    mgr = owm.weather_manager()
    weather = mgr.weather_at_place('Novosibirsk, RU').weather  # get the weather at London,GB now
    
    # print("wind = "+str(weather.wind()["speed"])+" m/s")                  # {'speed': 4.6, 'deg': 330}
    # print("temperature = "+str(weather.temperature('celsius')["feels_like"])+" celsius")  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    # print("rain = "+str(weather.rain))                    # {}
    feels_like = weather.temperature('celsius')["feels_like"]
    
    bs.gen_new_speech("сейчас температура ощущается как {} градусов цельсия".format(feels_like))
    bs.new_voice_tell("")