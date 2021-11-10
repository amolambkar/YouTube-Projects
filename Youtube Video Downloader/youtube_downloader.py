#
# Program : Download Youtube Video Using Python
# Author : Amol Ambkar
#

# requirement : pytube

from pytube import YouTube

link = "https://www.youtube.com/shorts/o_lNprCZaBs"

try:
    yt = YouTube(link)
except:
    print("connection error")

print(yt.title)

video = yt.streams.filter(progressive=True)
video = video.get_highest_resolution()

video.download()
print("Video Downloaded")
