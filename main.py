# from email.policy import default
# from genericpath import exists
from pathlib import Path
# from tkinter import W
from pyyoutube import Api
from pytube import YouTube
# from PIL import Image
import os
# import cv2
import time
import multiprocessing
import webbrowser
from playsound import playsound

# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

api = Api(api_key="AIzaSyBk9wcgyarDqsbDekrZ0nfElN53pvlvbS8") 

# Checking for updates from the channel

if __name__ == '__main__':    
  
  # get infos about videos
  # playlist = api.get_playlist_items(playlist_id="PL6_iWvoCGAJm--GrgiAHz7H6oLQ0LM8dE", count= 15)
  # print(playlist.items[0].to_dict())
  # for p in playlist.items:
  #   print(p.snippet.publishedAt)
  print('-------------------------------')
  print('|M O N E Y  G E N E R A T O R |')
  print('-------------------------------')

  video_id = None

  video_title = 'unknown'

  request = 0
  
  print('Checking new videos from the channel...\n')
  while True:
    playlists_by_id = api.get_playlist_items(playlist_id="PL6_iWvoCGAJm--GrgiAHz7H6oLQ0LM8dE")

    length = len(playlists_by_id.items)
    if length > 0:       
      video_id_data = playlists_by_id.items[0].snippet.resourceId
      if video_id is None: video_id = video_id_data.videoId
      
      if video_id != video_id_data.videoId:
        video_title = playlists_by_id.items[0].snippet.title
        print('We got a new video:', video_title)
        video_id = video_id_data.videoId
        break   
  
    else: video_id = 'unknown'

    if request % 100 == 0: 
      print('Current video id: ', video_id)
      print('We tried this many times:', request)

    request += 1
    time.sleep(10)

  print('PREPARING THE MEAL')
  
  print('---------------------------------------\n')

  while True:
    try: 
      yt = YouTube(f"youtube.com/watch?v={video_id}")
      mp4_files = yt.streams.filter(file_extension="mp4")
      mp4_360p_files = mp4_files.get_by_resolution("360p")
      mp4_360p_files.download("videos")
      if Path(f'videos/{video_title.replace(",", "")}.mp4').is_file():
        print('SUCCESS: The file exists!')
        break
      time.sleep(10)
    except Exception as e:
      print(e)
      print('Error: let\'s try again 2 secs after...\n')
      time.sleep(10)

  print('W A K E  T H E  F U K  U P')
  print('---------------------------------------\n')
  p = multiprocessing.Process(target=playsound, args=("alarm_long.mp3",))
  p.start()
  input("press ENTER to stop playback")
  p.terminate()
  
  print('LET\'S FKING GOOOOOOOOOO!!!')
  print('---------------------------------------\n')
  webbrowser.open('https://www.amazon.com/gp/css/gc/payment')
  os.startfile(Path(f'videos/{video_title}.mp4'))


# Downloading the video

# print('Downloading video...')

# Extracting images from video

# print('Extracting images from video...')

# vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
# success,image = vidcap.read()
# count = 0
# while success:
#   cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
#   success,image = vidcap.read()
#   print('Read a new frame: ', success)
#   count += 1

# Transforming the images for use

# print('Transforming images for Tesseract...')

# image_path = 'images\\'

# image_transformed_path = 'images\\transformed\\'

# image_name = 'easy.png'

# file_type = '.png'

# img = Image.open(os.path.join(image_path, image_name))

# img.show()

# for x in range(0, 360, 40):
#     transformedImg = img.rotate(x)
#     transformed_name = f'{x}_{image_name}'
#     print(transformed_name)
#     transformedImg.save(os.path.join(image_transformed_path, transformed_name))


# Analyzing image

# print('Analyzing image with Tesseract...')

# for x in range(0, 360, 40):
#     image = Image.open(os.path.join(image_transformed_path, f'{x}_{image_name}'))
#     print(f'Gift code (angle: {x}):', pytesseract.image_to_string(image))

# print('Redeeming gift cards on Amazon...')



# print('A total of X gift cards have been redeemed.')


