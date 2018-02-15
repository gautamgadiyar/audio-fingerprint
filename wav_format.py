import wave
from scipy import signal
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import scipy.io.wavfile
import numpy as ny
read=wave.open(r"piano2.wav",'r')
(rate,data)=scipy.io.wavfile.read(r"piano2.wav")

length = read.getnframes()      #get no of audio frames
n=1024
window=ny.hamming(n)        #for smoothening the curve and remove discontinuity

fs = read.getframerate()        #frames/sample per second
ts = 1.0/fs
m=length//n         #divide frames into groups of 1024
duration = length / float(fs)
#print m, length,fs
n1=read.getnchannels()
fsize=fs*n
a=ny.array(data)
#print data,rate,ts
data1=[]
data2=[]

for i in range (length):
    data1.append(a[i,0])
    data2.append(a[i,1])

b=ny.empty([m,n],dtype= complex)
c=ny.empty([m,n],dtype= complex)
res1=ny.empty([m,n],dtype= complex)
res2=ny.empty([m,n],dtype= complex)

for i in range(0,m):
    b[i,:] = data1[(i)*n:(i+1)*n]
    c[i,:] = data2[(i)*n:(i+1)*n]
data11=[]

for i in range(0,m):
    res1[i,:]=fft(b[i,:]*window)
    #res2[i,:]=fft(c[i,:]*window)
    for j in range(0,n):
        data11.append((res1[i,j]))
#res1[0:]=fft(data1*window)
outf1=[]
time, frq = ny.shape(res1)
freqs = ny.abs(ny.fft.fftfreq(frq, 1.0/n))

outf = 20*ny.log10(ny.abs(res1)) 

time, frq = ny.shape(outf)
plt.figure(figsize=(13, 7))
plt.imshow(ny.transpose(outf), aspect="auto")

plt.xlabel("time (s)")
plt.ylabel("frequency (hz)")
plt.xlim([0, time])
plt.ylim([0, frq/2])

plt.show()
plt.clf()
