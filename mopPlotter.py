"""
spceficallly for a disc and saving naming the files same as the .wav file
"""
import pandas as pd
import numpy as np
import librosa as lr
from glob import glob
import matplotlib.pyplot as plt
import os
os.chdir("tt")
os.chdir("9")
print(os.getcwd())
print(os.getcwd())
a = r"C:\Users\Salil Saxena\Desktop\Audio_Speech_Actors_01-24"
files = glob(a+"\\*")
len(files)
f =[]
for i in files:
    f+=glob(i+"\\*")
len(f)
print(f)
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
    plt.plot(time,audio)
    plt.set(xlabel = "Time (s)",ylabel = "Sound amplitude")
    plt.savefig(z[i]+".png")
    print("figue",i,"plotted")
    count+=1
    plt.close()
