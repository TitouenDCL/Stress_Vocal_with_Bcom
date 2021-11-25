import numpy as np
import matplotlib
import scipy
import tqdm
import sklearn
import plotly
import pyAudioAnalysis
from sklearn.model_selection import train_test_split

from pyAudioAnalysis import audioTrainTest as aT

##[Fs, x] = audioBasicIO.read_audio_file("DataBase/Fearfull/03-01-06-01-01-01-03.wav")

aT.extract_features_and_train(["DataBase/Fearfull/RAVDES","DataBase/Neutral"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "FearSVM")


