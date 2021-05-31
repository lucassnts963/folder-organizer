import sys
import time
import os
import platform

from watchdog.observers import Observer
from event_handler import MyEventHandler

if __name__ == '__main__':
	path = '/storage/emulated/0/Download'
	event_handler = MyEventHandler()
	observer = Observer()
	observer.schedule(event_handler, path, recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(1)
	finally:
		observer.stop()
		observer.join()
	