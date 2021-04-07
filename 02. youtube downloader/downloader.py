from pytube import YouTube

"""
https://www.youtube.com/watch?v=PT2_F-1esPk
"""

# link = input("Enter the link: ")
link = "https://www.youtube.com/watch?v=PT2_F-1esPk"
yt = YouTube(link)


print("Title: ", yt.title)                          # Title of video
print("Number of views: ", yt.views)                # Number of views of video
print("Length of video: ", yt.length, "seconds")    # Length of the video
# print("Description: ", yt.description)              # Description of video
print("Ratings: ", yt.rating)                       # Rating
print(yt.streams.first())                                   # printing all the available streams
