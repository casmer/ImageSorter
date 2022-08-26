from asyncio.windows_events import NULL
from contextlib import nullcontext
import re
import os
import os.path
import shutil
from types import NoneType
import exifread
debugmode=False

if debugmode == True:
    # Path for sorted files to be stored
    dirs_path = "D:\\Sorted\\"
    # Where images to be organized are located
    images_path = "D:\\TestDir\\"
else:
    # Path for sorted files to be stored
    dirs_path = "Z:\\casey\\OneDrive\\Pictures\\Camera Roll\\"
    # Where images to be organized are located
    images_path = "Z:\\casey\\OneDrive\\Pictures\\Camera Roll\\2018\\kristy"


# If it doesn't exist, creates a new one
if not os.path.exists(dirs_path):
    os.mkdir(dirs_path)


fail_count = 0
success_count = 0
move_count=0
nomove_count=0
# Recursively walk through all subdirectories and store the path + name of the jpg images
images = []
# for root, dirs, files in os.walk(images_path):
#     for f in files:
for f in os.listdir(images_path):
    # I'm only interested in pictures
    if f.endswith(".jpg") or f.endswith(".mp4") or f.endswith(".gif") or f.endswith(".png") or f.endswith(".jpeg") or f.endswith(".webp") or f.endswith(".JPG") :
        images.append(os.path.join(images_path, f))

# Extracts the date an image was taken and moves it to a folder with the format YYYY.MM.DD
# If the image doesn't have EXIF tags, sends it to a folder named 0000
for img in images:
    img_file_name = os.path.basename(img)
    date_string_search = re.search('[0-9]{8}', img_file_name)
    if date_string_search is not None and img_file_name.startswith("FB_IMG") == False and img_file_name.startswith("received") == False :
        success_count += 1
        date_string = date_string_search.group()
        date_path = date_string[0:4] + "\\" + date_string[4:6] 
    else:
        with open(img, "rb") as file:
            tags = exifread.process_file(file, details=False, stop_tag="DateTimeOriginal")
            try:
                date_path = str(tags["EXIF DateTimeOriginal"])[:7].replace(":", "\\")
                success_count += 1
            except:
                print(str(img) + " does not have EXIF tags.")
                
                
                fail_count += 1
                if img_file_name.startswith("FB_IMG"):
                    date_path = "Facebook"
                else:
                    date_path = "0000"

        
    if not os.path.exists(dirs_path + date_path):
        print("Creating Path {}".format(dirs_path + date_path))
        os.makedirs(dirs_path + date_path)
    # Second parameter is specific to my situation and must be changed...
    # In my case, the image name (including ".jpg") only used the last 12 chars of the string
    if (img_file_name.endswith(".webp")):
        img_to=dirs_path + date_path + "\\" + img_file_name[0:-4] + "jpg"   
    else:
        img_to=dirs_path + date_path + "\\" + img_file_name
    if (os.path.join(img_to) != img):
        print ("{} move to {}".format(img, img_to))
        shutil.move(img, img_to)
        move_count+=1
    else:
        #print ("{} is already where it should be".format(img))
        nomove_count+=1

print("Sorted " + str(success_count) + " files.") # Images properly sorted by date taken
print("Failed to sort " + str(fail_count) + " files.") # Images sent to 0000
print("Moved {} files".format(move_count))
print("Skipped {} files".format(nomove_count))