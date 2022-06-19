import commands.commands as c
import assistant.assistant_speeching as bs

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

# подготовка корпуса для распознавания запросов пользователя с некоторой вероятностью
# (поиск похожих)
vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 3))
classifier_probability = LogisticRegression()
classifier = LinearSVC()

def prepare_corpus():
    """
    Подготовка модели для угадывания намерения пользователя
    """
    corpus = []
    target_vector = []
    for intent_name, intent_data in c.commands["intents"].items():
        for example in intent_data["examples"]:
            corpus.append(example)
            target_vector.append(intent_name)

    training_vector = vectorizer.fit_transform(corpus)
    classifier_probability.fit(training_vector, target_vector)
    classifier.fit(training_vector, target_vector)


def get_intent(request):
    """
    Получение наиболее вероятного намерения в зависимости от запроса пользователя
    :param request: запрос пользователя
    :return: наиболее вероятное намерение
    """
    best_intent = classifier.predict(vectorizer.transform([request]))[0]

    index_of_best_intent = list(classifier_probability.classes_).index(best_intent)
    probabilities = classifier_probability.predict_proba(vectorizer.transform([request]))[0]

    best_intent_probability = probabilities[index_of_best_intent]
    
    print("best_intent_probability = "+str(best_intent_probability))
    # при добавлении новых намерений стоит уменьшать этот показатель
    if best_intent_probability > 0.36:
        return best_intent
    
def exec(voice_input):
    # отделение команд от дополнительной информации (аргументов)
    if voice_input:
        voice_input_parts = voice_input.split(" ")

        # если было сказано одно слово - выполняем команду сразу 
        # без дополнительных аргументов
        if len(voice_input_parts) == 1:
            intent = get_intent(voice_input)
            if intent and (intent != "приветствие" and bs.hello):
                c.commands["intents"][intent]["responses"]()
            elif intent and (intent == "приветствие" and not bs.hello):
                c.commands["intents"][intent]["responses"]()
            else:
                c.commands["failure_phrases"]()

        # в случае длинной фразы - выполняется поиск ключевой фразы 
        # и аргументов через каждое слово,
        # пока не будет найдено совпадение
        if len(voice_input_parts) > 1:
            for guess in range(len(voice_input_parts)):
                intent = get_intent((" ".join(voice_input_parts[0:guess])).strip())
                if intent and (intent != "приветствие" and bs.hello):
                    command_options = [voice_input_parts[guess:len(voice_input_parts)]]
                    c.commands["intents"][intent]["responses"](*command_options)
                    break
                if not intent and guess == len(voice_input_parts)-1:
                    c.commands["failure_phrases"]()