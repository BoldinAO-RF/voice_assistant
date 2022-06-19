import os, shutil
import winshell

dir_paths = {
        "temp": os.path.expanduser('~/AppData/Local/Temp'),
        "download": os.path.expanduser('~/Downloads')
    }


def clear_temporary_folder(*args: tuple):
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    except:
        print("Корзина уже пуста")

    for dir in dir_paths.values():
        for the_file in os.listdir(dir):
            file_path = os.path.join(dir, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(e)