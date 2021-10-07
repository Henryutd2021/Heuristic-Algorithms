from pytube import YouTube
from pytube import Playlist

# pl = Playlist("https://www.youtube.com/watch?v=RrmHbyLr8a8&list=PLkvG4EWPDB0n4iJv_aKylIUw_iBQQnYxh")
# pl.download_all(r'E:/kite')
# for i in range(2,46):
#     YouTube('https://www.youtube.com/watch?v=RrmHbyLr8a8&list=PLkvG4EWPDB0n4iJv_aKylIUw_iBQQnYxh&index='+ str(i)).streams.first().download(r'E:/kite')

#print(pl.video_urls)

# for i in pl.video_urls:
#     YouTube(i).streams.first().download(r'E:/kite')


YouTube('https://www.youtube.com/watch?v=QZmsKGpbGsM&t').streams.first().download()