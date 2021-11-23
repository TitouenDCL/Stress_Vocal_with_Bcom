from AudioListener import record
import numpy as np
import matplotlib
import scipy
import tqdm
import sklearn
import plotly
import pyAudioAnalysis
import time
from pyAudioAnalysis import audioTrainTest as aT
it = 10

for i in range(it):
     record("tralala.wav")
     start= time.time()
     stress = (aT.file_classification("tralala.wav", "FearSVM", "svm")[1][0])*100
     print(f"temps de calcul: {time.time()-start}")
     print(f"niveau de stress : {int(stress)}%")

