import os
import subprocess

AUDIO = ['aac','mp3','ogg','wma','alac','flac','aiff','pcm','wav']
VIDEO = ['mp4','flv','avi','wmv','rmvb','mpeg','mkv']
DOCS  = ['txt','doc','pdf','ppt','docx','csv','xls','xlsx']
IMAGE = ['jpg','jpeg','png','gif']
OTHERS = ['zip']


class FileHandler:
	path = '/storage/emulated/0/Download'
	folders_files = []
	audio_list = []
	video_list = []
	docs_list = []
	image_list = []
	others_list = []
	
	def __init__(self, path):
		self.path = path
		self.folders_files = os.listdir(path)
		
	def get_extension(self, filename):
		aux = filename.split('.')
		return aux[-1].casefold()
		
	def match(self, extension, list):
		for i in list:
			if i == extension.casefold():
				return True
		return False

	def run(self):
		for file in self.folders_files:
			extension = self.get_extension(file)
			if self.match(extension, AUDIO):
				self.move_file('Audio', file)
			elif self.match(extension, VIDEO):
				self.move_file('Video', file)
			elif self.match(extension, DOCS):
				self.move_file('Docs', file)
			elif self.match(extension, IMAGE):
				self.move_file('Image', file)
			else:
				self.move_file('Others', file)
		
	
	def move_file(self, folder, file):
		self.create_folder(folder)
		if os.path.isfile('{}/{}'.format(self.path,file)):
			subprocess.run(['mv','{}/{}'.format(self.path, file), '{}/{}'.format(self.path, folder)])
	
	def create_folder(self, folder):
		path = '{}/{}'.format(self.path, folder)
		if not os.path.exists(path):
			subprocess.run(['mkdir',path])
		return path
			