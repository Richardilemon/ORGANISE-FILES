#This python script automatically arranges the files in your folder
#The files will be grouped according to their file type
#The file type that can be grouped are audios, videos, images, and documents
import os
from pathlib import Path
FILETYPE = {
    "AUDIO":['.m4a','.m4b','.mp3','.wav','.flac','.cda'],
    "DOCUMENTS": ['.pdf','.rtf','.txt','.odt','.ppt'],
    "VIDEOS": ['.mov','.avi','.mp4','.wmv','.flv','.ogv','.mkv','.m4v','.3gp'],
    "IMAGES": ['.jpg','.jpeg','.png']
}
def SELECTFILETYPE(value):
    for file_format, extensions in FILETYPE.items():#This line is used to assign variables to the key and values in the dictionary
        for extension in extensions :
            if extension == value :
                return file_format
    return 'MISC' #This is for if the filetype and file extension is not added to the dictionary

def ORGANIZEFILE():
    for item in os.scandir():#scandir() calls the OS directory iteration system calls to get the names of the files in the given path
        if item.is_dir():#is_dir is basically used to check if the given path is an existing directory or not
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = SELECTFILETYPE(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

ORGANIZEFILE()
