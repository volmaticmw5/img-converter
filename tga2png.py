import sys
import os
from PIL import Image
#

# Validate required arguments
if len(sys.argv) < 3:
    print("Failed to convert: insuficient arguments, please specify a source and a output directory")
    quit()

# Get arguments
convert_counter = 0
source_dir = sys.argv[1]
target_dir = sys.argv[2]

print('Converting all images inside source directory to png and exporting them in the output directory with the following configurations:')
print('Source directory: ', source_dir)
print('Target output directory: ', target_dir)

# Convert from targa to png
def convert(filename):
    global convert_counter
    filepath_components = filename.split('/')
    filename_components = filepath_components[1].split('.') 

    if len(filepath_components) > 2:
        filename_components = filepath_components[len(filepath_components) - 1].split('.') 
        filename_export = filepath_components[len(filepath_components) - len(filename_components)] + '/' + filename_components[0] + '.png'
        folder_in_export = filepath_components[len(filepath_components) - 2]

        # Create dir if not exists in export
        if not os.path.exists(target_dir + '/' + folder_in_export):
            os.mkdir(target_dir + '/' + folder_in_export)

        image = Image.open(filename)
        image.save(target_dir + '/' + filename_export, compression=None)

        print('Converted TGA from', filename , 'to PNG ('+ target_dir + '/' +filename_export+')')
        convert_counter+=1
    else:
        image = Image.open(filename)
        image.save(target_dir + '/' +filename_components[0]+'.png', compression=None)

        print('Converted TGA from', filename , 'to PNG ('+ target_dir + '/' +filename_components[0]+'.png)')
        convert_counter+=1

# Loop through source directory files and sub directories
def convert_in_directory(dir):
    for filename in os.listdir(dir):
        file = os.path.join(dir, filename)
    
        if os.path.isfile(file):
            convert(file)
        else:
            convert_in_directory(file)

# Start with source directory
convert_in_directory(source_dir)

print("#######################################")
print("Done! Converted", convert_counter, "targa files to png!")
