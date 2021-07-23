from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

folder_to_track = "F:\\Python 工作室学习\\requests_01"
folder_destination_forWatching_csv = "F:\\Python 工作室学习\\WeatherData\\csv"
folder_destination_forWatching_xls = "F:\\Python 工作室学习\\WeatherData\\xls"


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):

        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "\\" + filename
            if filename.endswith("csv"):
                new_destination = folder_destination_forWatching_csv + "\\" + filename
                time.sleep(3)
                os.rename(src, new_destination)
                for filename in os.listdir(folder_to_track):
                    src = folder_to_track + "\\" + filename
                    if filename.endswith("xls"):
                        new_destination = folder_destination_forWatching_xls + "\\" + filename
                        os.rename(src, new_destination)
                        break
                break
            # if filename.endswith("xls"):
            #     new_destination = folder_destination_forWatching_xls + "\\" + filename
            # elif filename.__contains__("肖秀荣"):
            #     new_destination = folder_destination_kaoyan + "\\"+filename


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(3)
except KeyboardInterrupt:
    observer.stop()

observer.join()
