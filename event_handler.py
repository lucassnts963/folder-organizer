import os

from watchdog.events import FileSystemEventHandler

from file_handler import FileHandler

class MyEventHandler(FileSystemEventHandler):
	file_handler = FileHandler('/storage/emulated/0/Download')
	file_handler.folders_files = os.listdir(file_handler.path)
	file_handler.run()
	
	def moved(self):
		self.file_handler.folders_files = os.listdir(self.file_handler.path)
		self.file_handler.run()
	  
	
	def catch_all_handler(self, event):
		pass
 
	def on_moved(self, event):
		print("MOVED ")
		self.moved()
		self.catch_all_handler(event)
 
	def on_created(self, event):
		print("CREATED ")
		self.moved()
		self.catch_all_handler(event)
 
	def on_deleted(self, event):
		print("DELETED ")
		self.moved()
		self.catch_all_handler(event)
 
	def on_modified(self, event):
		print("MODIFIED ")
		self.moved()
		self.catch_all_handler(event)
