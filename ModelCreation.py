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


from pyAudioAnalysis import audioTrainTest as aT

[Fs, x] = audioBasicIO.read_audio_file("DataBase/Fearfull/nicolas add/MISSING TODDLERS_ Biological mom expresses her worries - 1of3 - 3of6.mp3")

aT.extract_features_and_train(["DataBase/Fearfull/all","DataBase/Neutral/all"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "FearSVM")


