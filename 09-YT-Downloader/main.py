from pytubefix import YouTube
url = input("Video URL: ")
YouTube(url).streams.filter(only_audio=True).first().download(filename="song.mp3")
print("Downloaded as song.mp3")