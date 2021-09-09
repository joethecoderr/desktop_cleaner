import os 
import re

def clean_downloads_images():
    from_ = "/Users/jgaspar/Downloads/"
    to_ = "/Users/jgaspar/Pictures/download_pictures/"
    try: 
        for f in os.listdir(from_):
            if re.search(".*\.(png|jpe?g|gif)$", f):
                os.replace(from_+str(f), to_+str(f))
                print(from_+str(f), to_+str(f))
    except FileNotFoundError:
        print("Archivos no encontrados")
    print("images moved")

def clean_downloads_documents():
    from_ = "/Users/jgaspar/Downloads/"
    to_ = "/Users/jgaspar/Documents/download_documents/"
    try: 
        for f in os.listdir(from_):
            if re.search(".*\.(docx?|pdf)$", f):
                os.replace(from_+str(f), to_+str(f))
    except FileNotFoundError:
        print("Archivos no encontrados")
    print("Files moved")