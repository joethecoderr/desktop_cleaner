import os
import re
from datetime import datetime

def clean_destkop_screenshots():
    dir = "/Users/jgaspar/Desktop/desktop_cleaner/src/cleaners"
    dir2 = "/Users/jgaspar/Desktop"
    for f in os.listdir(dir2):
        if re.search("^Screen.*\.(png)$", f):
            whole_path = os.path.join(dir2, f)
            timestamp_file = datetime.fromtimestamp(os.path.getmtime(whole_path)).date()
            present = datetime.now().date()
            difference = present - timestamp_file
            if difference.days >= 5: 
                os.remove(os.path.join(dir2, f))
    print("Done")

