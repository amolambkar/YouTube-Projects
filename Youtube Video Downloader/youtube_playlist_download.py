#
# Program : Download Youtube Playlist Using Python
# Author : Tech Blooded
#

# requirement : pytube

from pytube import Playlist , YouTube

# playlist link
link = "https://www.youtube.com/playlist?list=PLl2gq7invFLAQBvlPhS_U7xXwZb5kfR5Y"

try:
    play = Playlist(link)
except:
    print("connection error")

video_list = play.video_urls

for video_link in video_list:
    try:
        yt = YouTube(video_link)
    except:
        print("connection error")
    video = yt.streams.filter(progressive=True)
    video = video.get_highest_resolution()

    video.download()

print("Playlist Downloaded")