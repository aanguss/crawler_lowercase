import glob, os, shutil, mmap

print("this is so exciting... let's find files and folders! :)")
# os.chdir("/test_folder")

# def crawl(start_dir):    
#     # for root, dirs, files in os.walk(start_dir):
#     for dir in dirs:
#         print("found directory:" + dir + " renamed to: " dir.lower())
#         os.rename(os.path.join(os.getcwd(), dir), os.path.join(os.getcwd(), dir.lower())
#         crawl(dir.lower())
#     for file in files:
#         print("found file: " + file)
#         # if file.endswith(".txt"):
#         #      print(os.path.join(root, file))
#         # os.rename(file, file.replace(' ', '_').lower())
#         # os.rename(file, file.lower() + "temp")
#         # os.rename(file, file.lower())
#         # shutil.move(file, file.lower() + "temp")
#         # shutil.move(file, file.lower() - "temp")

#         # root, ext = os.path.splitext(file)
#         # print("Renaming", file, "to", root.lower())
#         # os.rename(os.path.join(os.getcwd(), file), os.path.join(os.getcwd(), file.lower()))

# crawl("tfc")


def lowercase_rename( dir ):
    # renames all subforders of dir, not including dir itself
    def rename_all( root, items ):
        for name in items:
            try:
                os.rename( os.path.join(root, name), 
                                    os.path.join(root, name.lower()))
            except OSError:
                pass # can't rename it, so what

    # starts from the bottom so paths further up remain valid after renaming
    for root, dirs, files in os.walk( dir, topdown=False ):
        rename_all( root, dirs )
        rename_all( root, files)

def lowercase_includes( dir ):
    def rename_includes( root, items ):
        for name in items:
            try:
                # with open(items, 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access.ACCESS_READ) as s:
                #     if s.find("#include \""):
                #         s = s.lower()
                # print("checking file: " + name)
                # if os.path.getsize(name) > 0:
                print ("file: " + name + ", size: " \
                        + str(os.path.getsize(os.path.abspath(os.path.join(root, name)))))
                        # + os.path.getsize(os.path.abspath(name)))
                        #+ os.stat(os.path.abspath(name)).st_size > 0)
                # print (os.stat(os.path.abspath(name)).st_size)
                
                # print (str(os.path.getsize(os.path.abspath(name))))
                

                if os.path.getsize(os.path.abspath(os.path.join(root, name))) > 0: #os.path.getsize(name) > 0:
                    # print("checking file: " + name)
                    # print (str(os.path.getsize(os.path.abspath(os.path.join(root, name)))))
                    with open( os.path.abspath(os.path.join(root, name)), 'w') as fileinput:
                        for line in fileinput:
                            print("found upper case on: " + line)
                            # if line[:9] == "#include \"":
                            if "#include" in line:
                                line = line.lower()
                                print("new line: " + line)
                                fileinput.write(line)
            # except OSError:
            except Exception as err:
                print("An exception happened: " + str(err))
                # print("error")
                pass
    
    for root, dirs, files in os.walk( dir, topdown=False ):
        rename_includes( root, files )

lowercase_rename("tfc")
lowercase_includes("tfc")