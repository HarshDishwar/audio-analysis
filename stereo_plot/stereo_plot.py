import wave
import numpy as np
file=wave.open('harvard.wav','rb')
import matplotlib.pyplot as plt


s_rate=file.getframerate()
n_frames=file.getnframes()

# to check whether the audio is mono or stereo
file.getnchannels() 
data = file.readframes(-1)

# since the audio data is in binary form we have to convert it into interger
w_data = np.frombuffer(data,np.int16) 

#then reshape the array into two dimension 
w_data.shape=-1,2 
print(w_data)

# one row for one channel and the other row for second
w_data = w_data.T 

print('Samppling rate :',s_rate)
print('No of frames :',n_frames)


# total dusration of audio sample
n_frames/float(s_rate)

duration=1/s_rate

# to get the time sequence
t_seq=np.arange(0,n_frames/float(s_rate),duration)

# graph of first channel
plt.plot(t_seq,w_data[0])
font1 = {'family':'serif','color':'darkred','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.ylabel('audio',fontdict=font1)
plt.xlabel('time (sec)',fontdict=font2)
plt.show()


# graph for second channel
plt.plot(t_seq,w_data[1],color='orange')
font1 = {'family':'serif','color':'darkred','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.ylabel('audio',fontdict=font1)
plt.xlabel('time (sec)',fontdict=font2)

plt.show()
