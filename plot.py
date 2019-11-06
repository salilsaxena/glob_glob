"""

"""
import pandas as pd
import numpy as np
import librosa as lr
from glob import glob
import matplotlib.pyplot as plt
import os
os.chdir("tt")
"""
 must conatain the dir where you want to save
 and that dir must have 1-24 dirs
"""
#
#
#
# os.chdir("9")
print(os.getcwd())
print(os.getcwd())
a = r"C:\Users\Salil Saxena\Desktop\Audio_Speech_Actors_01-24"
files = glob(a+"\\*")
len(files)
f =[]
for i in files:
    f+=glob(i+"\\*")
len(f)
# print(f)
def indexfinder(array):
    ind = []
    x = array.find("03")
    for i in array:
        if i=='.':
            break
    ind= [x,array.index(i)]
    return ind
start = indexfinder(f[0])[0]
end = indexfinder(f[0])[1]
# i=66
z=[]
for j in range(0,len(f)):
        z+=[f[j][start:end]]
        # print(f[j][i-1:])
        # z+=[f[j][i-1:len(f[0])-4]]

audio_files = f
len(audio_files)
count = 0
dir = 1
os.chdir('1')
for i in range(0,len(audio_files)):
    if count>59:
        dir+=1
        count=0
        os.chdir('..')
        os.chdir(str(dir))
    audio, sfreq = lr.load(audio_files[i])
    time = np.arange(0,len(audio))/sfreq
    # fig,ax = plt.subplots()
    plt.plot(time,audio)
    plt.xlabel("Time (s)")
    plt.ylabel("Sound amplitude")
    plt.savefig(z[i]+".png")
    print("figue",i,"plotted")
    count+=1
    plt.close()
# print(k)
