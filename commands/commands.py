import assistant.assistant_speeching as bs
import func.external.browser.browser as brows
import func.internal.files_and_directory.system_clear as system_clear

commands = {
    "intents": {
        "приветствие": {
            "examples": ["привет", "здравствуй", "добрый день"],
            "responses": bs.listen
        },
        "очистка": {
            "examples": ["удали временные файлы", "почисти компьютер", "удали временные файлы"],
            "responses": system_clear.clear_temporary_folder
        },
        "гугл": {
            "examples": ["найди в гугл", "google"],
            "responses": brows.search_for_google
        },
        "youtube": {
            "examples": ["найди в youtube", "youtube", "видео youtube"],
            "responses": brows.search_for_video_on_youtube
        },
        "погода": {
            "examples": ["погода", "что с погодой", "какая погода", "сколько градусов", "погода сегодня"],
            "responses": brows.weather
        }
    },
    "failure_phrases": bs.command_not_found
}