"""Script to zip important files using python"""

import os
import time

path = input("Enter the path of the files you want to back up:")
destpath = input("Enter the destination path of the files you want to back up:")

# listing out all the files in a path.
filelist = os.listdir(path)
print(filelist)

#Spliting the user input in a seperate list
selec = input("Enter the files you want to backup")
lst = selec.split(",")

#Creating a directory if not already present
if not os.path.exists(destpath):
    os.mkdir(destpath)

#Checking if the file name entered is in filelist. If not show a error and continue.
for i in lst:
    if i in filelist:
        target = destpath + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
        zip_command = 'zip -r {} {}'.format(target, ''.join(path))
        print('Zip command is:')
        print(zip_command)
        print('Running:')
        if os.system(zip_command) == 0:
            print('Successful backup to', target)
        else:
            print('Backup FAILED')

    else:
        print("Error: {} is not in the folder. Process continued".format(i))
        continue


