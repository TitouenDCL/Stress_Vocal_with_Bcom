import numpy as np
import matplotlib
import scipy
import tqdm
import sklearn
import plotly
import pyAudioAnalysis
from sklearn.model_selection import train_test_split
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import MidTermFeatures
import matplotlib.pyplot as plt
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import MidTermFeatures
import matplotlib.pyplot as plt
from pyAudioAnalysis import audioTrainTest as aT
import os


""" This code was made to extract the features of the audio before training on them, and
then training on the features with SKlearn

But we've aborted this option since we found that it was harder to use vectors as features
and that the PyAudioAnalysis was already doing this for us

We face some issues thought, since the size of the vectors (representing each features, 1vector=1feature) were 
not the same size because the length of the audio and it period of sample were not the same for
the differents audios

"""



content = "DataBase/Fearfull/mila add/audio4.wav"
nb_features = 137
size_features = 59
X = np.zeros([os.listdir("DataBase/Fearfull/RAVDES").__sizeof__() + os.listdir("DataBase/Neutral/RAVDES").__sizeof__(),
              nb_features, size_features])
# on remplie X avec les audio stressed
i = 0
for audio in os.listdir("DataBase/Fearfull/RAVDES"):
  [Fs, x] = audioBasicIO.read_audio_file(content)
  if len(x.shape)>1:
    x=x[:,0]
  mt,st,mt_names = MidTermFeatures.mid_feature_extraction(x, Fs, 0.1*Fs, 0.05*Fs,0.05*Fs,0.025*Fs)
  X[i,0] = np.ones([size_features])
  X[i,1:] = mt ## y=1
  i+=1

##on remplie X avec les audio neutral
for audio in os.listdir("DataBase/Neutral/RAVDES"):
    [Fs, x] = audioBasicIO.read_audio_file(content)
    if len(x.shape)>1:
        x = x[:, 0]
    mt,st,mt_names = MidTermFeatures.mid_feature_extraction(x, Fs, 0.1*Fs, 0.05*Fs,0.05*Fs,0.025*Fs)
    X[i,0] = np.zeros([size_features]) # y = 0
    X[i,1:] = mt
    i += 1

"""
plt.subplot(2,1,1); plt.plot(mt[1,:]); plt.xlabel('Frame no'); plt.ylabel(mt_names[1])
plt.subplot(2,1,2); plt.plot(mt[2,:]); plt.xlabel('Frame no'); plt.ylabel(mt_names[2])
plt.show()

"""
print(f"{X[0] = }")
print(f"{X[0].shape = }")
print(f"{X.shape = }")


""" On a créé un gros tableau avec, pour chaque audio, 136 vecteurs qui représentent les 136
features  (de size 60) et 1 vecteurs remplie de 0 ou de 1, qui indique si c'est un audio fearfull ou neutral

on a donc un array de shape : (nombre total d'audio)*(nombres de features = 136 + +1 (fear or neutral)
                                * (taille des vecteurs des features = 60 ici)
"""