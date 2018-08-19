import os
import sys
import shutil


def filename_trimmer():
    """ 
    Argument 1 is the source dir
    Argument 2 is the destination dir
    Argument 3 is the number of chars to trim off the end. Default is 16. 

    ex: python filenameTrimmer_v02.py /path/to/source/dir /path/to/dest/dir 16

    This is a simple script that trims the last 16 characters off of a filename.
    This is common file naming convention (including the video id) in some 
    online videos such as youtube, specifically youtube-dl downloads of youtube 
    clips.

    NOTE - A different way to fix this in youtube-dl is by re-downloading it 
    with these naming arguments.
    youtube-dl -o '%(title)s.%(ext)s' <URL>
    https://github.com/rg3/youtube-dl/issues/4071
    """
    
    source_path = sys.argv[1]
    dest_path = sys.argv[2]
    if len(sys.argv) > 3:
        print(len(sys.argv))
        trim_length = int(sys.argv[3])
    else:
        trim_length = 16

    for filename in os.listdir(source_path):
        print(filename[-4:])
        if filename[-4:] == ".mp4":
            if dest_path[-1] != '/':
                dest_path += '/'
            if source_path[-1] != '/':
                source_path += '/'
            try:
                newname = dest_path + str(filename[:-trim_length]) + ".mp4"
                filepath = source_path + filename
                print('copying from ' + filepath + ' -> ' + newname)
                shutil.copy2(filepath, newname)
            except:
                print('error on main routine:', sys.exc_info()[0])
                pass


filename_trimmer()
