import sys
import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.start_script()

    def start_script(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen([sys.executable, self.script])

    def on_any_event(self, event):
        if event.event_type in ('modified', 'created', 'deleted', 'moved'):
            self.start_script()

if __name__ == "__main__":
    script_to_watch = "views/admin-roles/dashboard-admin.py"  # Replace with your script
    event_handler = ChangeHandler(script_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)

    print(f"Watching for changes in '{script_to_watch}'")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
