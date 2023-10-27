import os
import time

files = [f for f in os.listdir() if(os.path.isfile(f))]
fileTypes = (".jpeg", ".jpg", ".png", ".tif", ".tiff", ".gif", ".esp", ".raw", ".cr2", ".nef", ".orf", ".sr2", ".webp")

for file in files:
    if(not file.lower().endswith(fileTypes)): continue
    
    # Get time created and transform into a time object
    time_created = os.path.getctime(file)
    time_object = time.strptime(time.ctime(time_created))
    
    # Transforming the time object to a timestamp 
    # of ISO 8601 format
    year = time.strftime("%Y", time_object)
    month = time.strftime("%B", time_object)

    # Try create a Year folder
    try: os.mkdir(year)
    except: pass
    
    # Try create the month in the year folder
    try: os.mkdir(year+"/"+month)
    except: pass
    
    try: os.rename(file, year+"/"+month+"/"+file)
    except: pass