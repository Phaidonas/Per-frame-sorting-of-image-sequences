from PIL import Image
import glob
import numpy as np
import cv2
from tkinter import filedialog
from tkinter import *
from PIL import Image
from moviepy.editor import *

import os


image_seg_1=''
image_seg_2=''
output_path=''



#Basic UI

# def browse_button(filename):
#     # Allow user to select a directory and store it in global var
#     # called folder_path
#     global folder_path
#     filename = filedialog.askdirectory()
#     folder_path.set(filename)
#     print(filename)
#
#
# root = Tk()
# folder_path = StringVar()
# lbl1 = Label(master=root,textvariable=folder_path)
# lbl1.grid(row=0, column=1)
# button2 = Button(text="Browse", command=lambda: browse_button(image_seg_1))
# button2.grid(row=2, column=4)
# button3 = Button(text="Browse", command=lambda: browse_button(image_seg_2))
# button3.grid(row=5, column=4)
# button4 = Button(text="Browse", command=lambda: browse_button(output_path))
# button4.grid(row=10, column=4)
#
# mainloop()


#Paths
image_seq_1='C:/Users/Phaid/Documents/Pool_Laptop/animation_khm/Renders/layer_1_test1/'
image_seq_2='C:/Users/Phaid/Documents/Pool_Laptop/animation_khm/Renders/layer_2_test1/'
output_path='C:/Users/Phaid/Documents/Pool_Laptop/Python/Frame_script/test_output/'

#if you want to export images or video, video does not work for now
export_images=True
export_vid=False

#Frames the image sequence you want to flicker 
number_of_frames=1




# image_list_1 = pims.open(r'C:\Users\Phaid\Documents\Pool_Laptop\Python\Frame_script\Test_folder_1/*.png')
# image_list_2 = pims.open(r'C:\Users\Phaid\Documents\Pool_Laptop\Python\Frame_script\Test_folder_2/*.png')
image_list_1=[]
image_list_2=[]

for filename_1 in glob.glob(r'{}*.png'.format(image_seq_1)):
    im=Image.open(filename_1)
    image_list_1.append(im)

for filename_2 in glob.glob(r'{}*.png'.format(image_seq_2)):
    im=Image.open(filename_2)
    image_list_2.append(im)

print(len(image_list_1))
print(len(image_list_2))


pos1=0
pos2=0



compined_array=[]

Array_imgs=[]

while len(compined_array)<len(image_list_1)+len(image_list_2):
    if not (pos1>len(image_list_1)-1):

        for count_1 in range(number_of_frames):
            compined_array.append(image_list_1[pos1+(count_1-1)])

        pos1+=number_of_frames

    if not (pos2>len(image_list_2)-1):
        for count_2 in range(number_of_frames):
            compined_array.append(image_list_2[pos2+(count_2-1)])
        pos2+=number_of_frames






for i in compined_array:
    arr=np.array(i)
    Array_imgs.append(arr)



fourcc = cv2.VideoWriter_fourcc('M','P','E','G')

height, width, layers = Array_imgs[0].shape

print(height)
print(width)
print(layers)

size= (width, height)

video = cv2.VideoWriter("Test_video.avi",fourcc , 24, size)

for image in Array_imgs:
    cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    video.write(image)
    print('done')

cv2.destroyAllWindows()
video.release()



#VIDEO EXPORT CODE

# height, width = 1024,768
# video = cv2.VideoWriter('{}video.mp4'.format(output_path), -1, 1,24, (width,height))
#
#
# for index,i in enumerate(compined_array):
#     if export_images==True:
#         i.save('{}{}.png'.format(output_path,index))
#         print('Remaining {} images of {} images'.format(len(compined_array)-index,len(compined_array)))
#     if export_vid==True:
#
#
#
#         transformed_img = np.array(compined_array[i])
#         print(transformed_img.shape)
#         video.write(transformed_img)
#
#
#
# cv2.destroyAllWindows()
# video.release()


print("video_export")

print(len(image_list_1)+len(image_list_2))
print(len(compined_array))
print("Done")

