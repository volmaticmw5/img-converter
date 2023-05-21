import sys
import os
from PIL import Image

# Validate required arguments
if len(sys.argv) < 5:
    print("Failed to convert: insuficient arguments, please specify a source and a output directory")
    print("command <source_dir> <source_format> <output_dir> <output_format>")
    quit()

# Get arguments
convert_counter = 0
source_dir = sys.argv[1]
source_format = sys.argv[2]
target_dir = sys.argv[3]
target_format = sys.argv[4]

# Validate formats
if target_format != "png" and target_format != "webp" and target_format != "tga" and source_format != "tga" and source_format != "png" and source_format != "webp":
    print('Unsupported format: ' + target_format + ' or ' + source_format)
    print('Please specify a valid format: png, webp, tga')
    quit()

print('Converting all images inside source directory from '+source_format+' to '+target_format+' and exporting them in the output directory with the following configurations:')
print('Source directory: ', source_dir)
print('Target output directory: ', target_dir)

# Convert from targa to desired format
def convert(filename):
    global convert_counter
    global source_format
    global target_format

    filepath_components = filename.split('/')
    filename_components = filepath_components[1].split('.') 

    if len(filepath_components) > 2:
        filename_components = filepath_components[len(filepath_components) - 1].split('.') 
        filename_export = filepath_components[len(filepath_components) - len(filename_components)] + '/' + filename_components[0] + '.'+target_format+''
        folder_in_export = filepath_components[len(filepath_components) - 2]

        # Create dir if not exists in export
        if not os.path.exists(target_dir + '/' + folder_in_export):
            os.mkdir(target_dir + '/' + folder_in_export)

        image = Image.open(filename)
        image.save(target_dir + '/' + filename_export, compression=None, format=target_format)

        print('Converted '+source_format+' from', filename , 'to '+target_format+' ('+ target_dir + '/' +filename_export+')')
        convert_counter+=1
    else:
        image = Image.open(filename)
        image.save(target_dir + '/' +filename_components[0]+'.'+target_format+'', compression=None, format=target_format)

        print(filename_components[0])
        print('Converted '+source_format+' from', filename , 'to '+target_format+' ('+ target_dir + '/' +filename_components[0]+'.'+target_format+')')
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
print("Done! Converted", convert_counter, source_format , "files to", target_format, "!")