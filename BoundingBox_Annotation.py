#This will be the step 3 of the project

# This code is used to merge all the indivisual YOLO files into one csv file for easy processing
# YOLO files and bounding boxes are created using "LabelImg"
import csv
import os

#Once we save all the yolo files indiviually we will concatinate all the yolo files in one csv which we can use for our models
#For that we need input of YOLO files and output location.
input_path = input("Enter the input folder path of YOLO files: ").rstrip()
output_csv_path = input("Enter the folder path & file name (with extension as .csv) to store the concat csv: ").rstrip()

with open(output_csv_path, 'w', newline='') as dbfile:
    writer = csv.writer(dbfile)

    # These will be the column names of the output csv.
    writer.writerow(['Filename', 'Data', 'Concat'])

    # We will now iterate through the input YOLO files
    for imagename in os.listdir(input_path):
        #We will skip the classes file which is generated by LabelImg as we know the what they stand for.
        """classes:
                    15 --> Adult
                    16 --> Child
                    17 --> Logo, etc"""
        if imagename.startswith('classes'):
            continue
        if imagename.endswith('.txt'):
            with open(os.path.join(input_path, imagename), 'r') as txtfile:
                lines = txtfile.readlines()

                # Extracting the data and saving it in the variable BBclasses (Bounding box classes)
                BBclasses = [line.strip() for line in lines]

                # Writing the data from BBclasses such that eagggggggch entry will be associated with the image name and the bounding box coordinates.
                for classes in BBclasses:
                    writer.writerow([imagename] + [classes] + [imagename + " "+ classes])

print(f'CSV is created and stored in {output_csv_path}')