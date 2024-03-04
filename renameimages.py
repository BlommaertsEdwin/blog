import os

path_dir = "static/images/walks/2"

# get all file names in the directory
for dir, subdirs, files in os.walk(path_dir):
    number = 0
    for f in files:
        number += 1
        # separating the file name and extension
        file_name = f.split('.')[0]
        ext = f.split('.')[-1]
        # new file name
        new_file_name = "walk2-" + str(number) + "." + ext
        os.rename(os.path.join(path_dir, f), os.path.join(path_dir, new_file_name))
        print("![Test](../../images/walks/2/%s) \n\b" % new_file_name)