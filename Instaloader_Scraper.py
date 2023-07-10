import instaloader
import sys
import lzma
import json
import os
import time
import shutil

# Create an instance of Instaloader
loader = instaloader.Instaloader()

"""As the user (Gillette India) has a public account we do not need
  username and password to access the account. Use the username without the @ tag."""
target_username = input("Enter target username: @")

# This will help us retrieve the profile of the target user
profile = instaloader.Profile.from_username(loader.context, target_username)

# loop through the profile to get all the posts
print("\n-------Temporary Directory created by Instaloader-------\n")
for post in profile.get_posts():
    # output will be stored in a temporary folder called "SocialMedia"
    loader.download_post(post, target=r'SocialMedia')

# Now we need to get the path for the "SocialMedia" folder so the we can use it for iterations.
currentfolder = os.getcwd()
savedfolder = 'SocialMedia'
srcfolder = os.path.join(currentfolder, savedfolder)
print(f"\n-------Source folder for the data is {srcfolder}-------")

# Creates an instance of the profile to check if the user is valid and has a public account
instaloader.Profile.from_username(loader.context, target_username)

# Creating a delay so that the program doesn't raise the exception of too many requests.
time.sleep(5)