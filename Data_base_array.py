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
