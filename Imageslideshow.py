from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

#List of image path
image_paths = [
    r".........................................",
    r"..............................................",
    r".................................................",
    r"...........................................",
    r"........................................................."  #r stands for ros string that does not allow \n
]

#Resize the images to 1080X1080
image_size=(700,700)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)
def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text='Play Slideshow', command = start_slideshow)
play_button.pack()

root.mainloop()  #It is the main function or a end path of every python prject