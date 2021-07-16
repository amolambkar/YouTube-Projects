#
# author - Amol Ambkar
# Program - Download Youtube video using python
#

from pytube import YouTube
import os

link="https://www.youtube.com/watch?v=KsCiH6aYZd8"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") 

print(yt.title)
stream = yt.streams.filter().first()
out_file = stream.download()

print(yt.title + " has been successfully downloaded.")
