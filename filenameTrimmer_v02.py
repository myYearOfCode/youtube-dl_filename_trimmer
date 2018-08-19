import os
import sys
import shutil
	'''
	this is run with two arguments passed in to the script.
	ex python filenameTrimmer_v02.py /path/to/source/dir /path/to/dest/dir
	'''

def filename_trimmer():
	''' Argument 1 is the source dir, argument 2 is the destination dir. 

	This is a simple script that trims the last 16 characters off of a filename. This is common file naming convention (including the video id) in some online videos such as youtube, specifically youtube-dl downloads of youtube clips.
	
	NOTE - A different way to fix this in youtube-dl is by re-downloading it with these naming arguments.
	youtube-dl -o '%(title)s.%(ext)s' <URL>
	https://github.com/rg3/youtube-dl/issues/4071
	'''
	source_path=sys.argv[1]
	dest_path=sys.argv[2]
	# print (dest_path)
	# print (source_path)


	for filename in os.listdir(source_path):
		print(filename[-4:])
		if filename[-4:]==".mp4":
			if dest_path[-1] != '/':
				dest_path += '/'
			if source_path[-1] != '/':
				source_path += '/'	
			try:
				newname=dest_path+str(filename[:-16])+".mp4"
				filepath=source_path+filename
				print ('copying from '+filepath+' -> '+ newname)
				shutil.copy2(filepath,newname)
			except:
				print ('error on main routine:' , sys.exc_info()[0])
				pass

filename_trimmer()