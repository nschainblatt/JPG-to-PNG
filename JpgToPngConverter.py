from PIL import Image, ImageFilter
import sys
import os

# grab first and second argument
image_folder = sys.argv[1]
new_image_folder = sys.argv[2]

# checking if new_image_folder exists
if os.path.exists(new_image_folder): 
    pass

# if not, this creates the desired folder in the image-playground folder
else:  
    os.mkdir(new_image_folder)

print(f'This is your directory: {os.getcwd()}')
# changes directory to image_folder
os.chdir(image_folder)

# loops through image_folder
for file in os.listdir():
    print(f'Converting: {file} to PNG!')
    # opens image
    convert = Image.open(file)
    # changes directory to save location
    os.chdir(f'../{new_image_folder}')
    # converts and saves image
    convert.save(file[:-4] + '.png', 'png')
    # changes directory back to image_folder
    os.chdir(f'../{image_folder}')
