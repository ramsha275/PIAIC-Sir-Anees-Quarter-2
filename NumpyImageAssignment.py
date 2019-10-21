# %%
import os
from PIL import Image
import numpy as np


# Set the directory you want to start from
rootDir = 'photos'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
    

# %%
main_list = []
im = Image.open(dirName+"\\"+fileList[0])
print("----------X------------X-----------------------X\n\n")
im.show()
original_array = np.array(im)
print(original_array.shape)
print(original_array.size)
print(original_array)
print("\n\n----------X------------X-----------------------X\n\n")
new_image = im.resize((200, 200))
resized_array = np.array(new_image)
print(resized_array.size)
print(resized_array.shape)
print(resized_array)
main_list.append(resized_array)

# %%
main_list

# %%
pic = 2
for i in range(1,len(fileList)):
    print("PIC NO : ",pic)
    im = Image.open(dirName+"\\"+fileList[i])           
    print("----------X------------X-----------------------X\n\n")
    im.show()
    original_array = np.array(im)
    print(original_array.shape)
    print(original_array.size)
    print(original_array)
    print("\n\n----------X------------X-----------------------X\n\n")
    new_image = im.resize((200, 200))
    resized_array = np.array(new_image)
    print(resized_array.size)
    print(resized_array.shape)
    print(resized_array)
    print("APPENDING TIME")
    main_list.append(resized_array)
    pic = pic+1

# %%
len(main_list)

# %%
main_list

# %%
def main():
    
    main_arr= np.array(main_list)
    print("FINAL NUMPY ARRAY :\n\n ",main_arr)
    return main_arr

# %%
# main_arr = main()
# main_arr

# %%
main_arr.shape

# %%
main_arr.ndim

# %%
main_arr.size

# %%
