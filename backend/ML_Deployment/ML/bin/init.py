import os,sys

def get_csv():
    if len(sys.argv) > 1 and sys.argv[1] != "":
        if(os.path.exists(sys.argv[1])):
            return sys.argv[1]
        print("",sys.argv[1], "not found")
        sys.exit(0)
    print("","Usage : python3 file.py path/to/csv")
    sys.exit(0)


def make_dirs(dirs:list):
    for dir in dirs:
        if not os.path.isdir(dir):
            os.mkdir(dir)