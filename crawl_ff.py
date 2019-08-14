import os, fileinput, argparse

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
                if os.path.getsize(os.path.abspath(os.path.join(root, name))) > 0:
                    for line in fileinput.input(os.path.abspath(os.path.join(root, name)), inplace=1):
                        if "#include " in line:
                            print(line.lower(), end='', flush=True)
            except Exception as err:
                print("An exception happened with file " + name + ": " + str(err))
                pass
    
    for root, dirs, files in os.walk( dir, topdown=False ):
        rename_includes( root, files )

def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', dest='dir',
                        type=str, help='the root directory in which to modify \
                        lowercase files/directories and found #includes')
    args = parser.parse_args()

    if args.dir is None:
        print("need to specify directory with -d or --directory")
        sys.exit(0)
    else:    
        lowercase_rename(dir)
        lowercase_includes(dir)
