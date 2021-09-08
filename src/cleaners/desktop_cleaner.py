from pathlib import Path
import glob
import os
import re

def clean_destkop(regex):
    print("Llegiue")
    # directory = "."
    dir = "/Users/jgaspar/Desktop/desktop_cleaner/src/cleaners"
    for f in os.listdir(dir):
        print(f)
        if re.search("^Screen.*\.(jpe?g|gif|png|tiff)$", f):
            os.remove(os.path.join(dir, f))
        else:
            print("No match found")

