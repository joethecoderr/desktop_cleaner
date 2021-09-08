import sys
import cleaners.desktop_cleaner as desk_cleaner

def select_folder(directory_name):
    if directory_name is not None:
        if directory_name == "desktop":
            desk_cleaner.clean_destkop("dddd")
        else:
            print(f"Case {directory_name} not implemented")
            
    else:
        print("No directory specified")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg_ = sys.argv[1]
        for folder in range(1, len(sys.argv)):
            select_folder(sys.argv[folder])
        