from pytube import YouTube
import pandas as pd

#where to save
SAVE_PATH = r"D:\reflexion\Frames\Videos" #to_do

data = pd.read_csv(r"D:\reflexion\Genre Task\qwerty.csv")
#link of the video to be downloaded
link = data['URL'].tolist()

for i in link:
	try:
		
		# object creation using YouTube
		# which was imported in the beginning
		yt = YouTube(i)
		yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
		yt.download(SAVE_PATH)
	except:
		
		#to handle exception
		print("Connection Error")
		print(str(i) + "......NOT DOWNLOADED")

	print(str(i) + ".....done")
	
print('Task Completed!')
