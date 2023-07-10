#This will be the step 2 of the project

import os
import lzma
import shutil
import json
from Instaloader_Scraper import srcfolder

# Code to store multidimentional data into folder
# Prefered to use folders due to performance advantage and easy data visualization for programmer.
# We are first going to input the output folder where all the data should be stored.
folder_path = input("Enter the folder path:").rstrip()
print("\n")

# Creating subfolders for jpg, mp4, Captions, json and jsonXZ
jpg_path = os.path.join(folder_path, "jpg")
if not os.path.exists(jpg_path):
    os.makedirs(jpg_path)

mp4_path = os.path.join(folder_path, "mp4")
if not os.path.exists(mp4_path):
    os.makedirs(mp4_path)

txt_path = os.path.join(folder_path, "TextCaptions")
if not os.path.exists(txt_path):
    os.makedirs(txt_path)

json_path = os.path.join(folder_path, "json")
if not os.path.exists(json_path):
    os.makedirs(json_path)

jsonXZ_path = os.path.join(folder_path, "jsonXZ")
if not os.path.exists(jsonXZ_path):
    os.makedirs(jsonXZ_path)

# Counter for json file extractions
counter = 1

# Iterate through the files in the folder and move files to their respective folders.
for filename in os.listdir(srcfolder):
    if filename.endswith('.jpg'):

        srcfile = os.path.join(srcfolder, filename)
        destfile = os.path.join(jpg_path, filename)

        shutil.move(srcfile, destfile)
        print(f"Moved {filename} to {jpg_path}")

    elif filename.endswith('.mp4'):

        srcfile = os.path.join(srcfolder, filename)
        destfile = os.path.join(mp4_path, filename)

        shutil.move(srcfile, destfile)
        print(f"Moved {filename} to {mp4_path}")

    elif filename.endswith('.txt'):

        srcfile = os.path.join(srcfolder, filename)
        destfile = os.path.join(txt_path, filename)

        shutil.move(srcfile, destfile)
        print("Moved {} to {}".format(filename, txt_path))

    # Extracting data from the .json.xz files which are compressed files to regular json files.
    elif filename.endswith('.json.xz'):
        # Constructing full file paths.
        file_path = os.path.join(srcfolder, filename)

        # Decompressing the JSON.xz file
        with lzma.open(file_path, 'rb') as f:
            json_data = f.read()

        # Constructing output file name
        base_name = os.path.splitext(filename)[0]
        output_file = os.path.join(json_path, f"{base_name}_{counter}.json")

        # Incrementing the counter so that the next file will get updated names and no duplicates.
        counter += 1

        # Loading the JSON data so that we can read it in a python dict format and deserialize the file.
        data = json.loads(json_data)

        # Saveing the data as JSON
        with open(output_file, 'w') as f:
            json.dump(data, f)

        print(f"Saved {output_file}")

        # moving the files to the respective jsonXZ folder after iteration.
        srcfile = os.path.join(srcfolder, filename)
        destfile = os.path.join(jsonXZ_path, filename)

        shutil.move(srcfile, destfile)
        print("Moved {} to {}".format(filename, jsonXZ_path))

# Condition to check if the srcfolder is different from temparory folder so that we can clean up the temporary files.
if srcfolder != folder_path:
    os.rmdir(srcfolder)
    print("\n-------Temporary directory created by Instaloader has been deleted-------")
    print(f"\n-------Scraped data is stored at {folder_path}------- ")

""" --------------------------------------------------------------------------------------------------
 --------------------------------------------------------------------------------------------------"""
