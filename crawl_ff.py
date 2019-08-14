import os, sys, fileinput, argparse

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

def valid_dir(name):
    if os.path.isdir(name):
        return name
    else:
        raise argparse.ArgumentTypeError(f"{name} is not a valid directory")


def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', dest='dir',
                        type=valid_dir, help='the root directory in which to modify \
                        lowercase files/directories and found #includes')
    args = parser.parse_args()

    print("This is so exciting...")
    if args.dir is None:
        print("need to specify directory with -d or --directory")
        sys.exit(0)
    else:
        dir = args.dir #os.path.abspath(args.dir)
        print(f"Let's find files and folders in {dir}!")
        lowercase_rename(dir)
        print("Now for the found #includes!")
        lowercase_includes(dir)
        print("... done 'n done :)")


# call main if this script is being called by itself
if __name__ == '__main__':
    _main()
