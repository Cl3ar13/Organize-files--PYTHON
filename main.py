import os
from utils import *

import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class MyEventHandler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        pass

    @staticmethod
    def on_modified(event):
        if is_file_txt(event) == True:
            foldername = to_make_folder("is_file_txt")
            move_file_corresponding_folder(event, foldername)

    @staticmethod
    def on_moved(event):
        pass


    @staticmethod
    def on_deleted(event):
        pass


# path
os.chdir("Insira\\Seu\\Diretorio\\de\\Downloads")

event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, os.getcwd(), recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()
    observer.join()
