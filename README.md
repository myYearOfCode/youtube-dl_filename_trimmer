# youtube-dl_filename_trimmer
This script trims the 16 character video-id from mp4 files downloaded using youtube-dl.

Argument 1 is the source dir, argument 2 is the destination dir. 

ex python filenameTrimmer_v02.py /path/to/source/dir /path/to/dest/dir

This is a simple script that trims the last 16 characters off of a filename. This is common file naming convention (including the video id) in some online videos such as youtube, specifically youtube-dl downloads of youtube clips.
	
NOTE - A different way to fix this in youtube-dl is by re-downloading it with these naming arguments.
youtube-dl -o '%(title)s.%(ext)s' <URL>
https://github.com/rg3/youtube-dl/issues/4071
