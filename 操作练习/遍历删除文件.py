import shutil

filelist = []
rootdir = "./2/2"
print filelist
shutil.rmtree(rootdir, True)
print "dir " + rootdir + " removed!"
