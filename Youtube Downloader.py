import pafy

url = input("Enter Link: ")
video = pafy.new(url)
streams=video.streams
best = video.getbest()
best.download()
print(best.resolution,best.extension)
