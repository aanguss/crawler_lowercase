import glob, os, shutil

print("this is so exciting... let's find files and folders! :)")
# os.chdir("/test_folder")

for root, dirs, files in os.walk("tfc"):
    for file in files:
        # if file.endswith(".txt"):
        #      print(os.path.join(root, file))
        # os.rename(file, file.replace(' ', '_').lower())
        # os.rename(file, file.lower())
        # os.rename(file, file.lower())
        shutil.move(file, file.lower())