#  imports
from pytube import YouTube

# url
url = 'https://www.youtube.com/watch?v=tb8gHvYlCFs'

# get the video from the url
video = YouTube(url)

# get the title
title = video.title

# print(title)

# downloading the video
stream = video.streams.first()

# downloading to cwd
stream.download()

print('Download Complete')
 #credits codewithbenny
