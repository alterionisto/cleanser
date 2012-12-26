import os
music = r"f:\music"
ext = "log txt m3u dat jpg jpeg"
for (path, dirs, files) in os.walk(music):
	for f in files:
		if os.path.splitext(f)[1][1:] in ext:
			try:
				print("file:", os.path.join(path, f))
				os.remove(os.path.join(path, f))
			except:
				print("error")
			#
	if not os.listdir(path):
		try:
			print("dir:", path)
			os.rmdir(path)
		except:
			print("error")
		#
#36,2 GB (38 907 429 316 bytes)
#3 308 Files, 653