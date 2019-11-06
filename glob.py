from glob import glob
a =r"C:\Users\Salil Saxena\Desktop\Audio_Speech_Actors_01-24" #this is our main dir
dirs  = glob(a+"\\*") #we accesssed sep dir inside our main dir
# dirs
files = []
for i in dirs:
    files+=glob(i+"\\*")
len(files)
# files is our list which contain our whole set of wave files
