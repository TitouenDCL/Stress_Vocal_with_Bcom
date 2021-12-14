from AudioListener import record
import numpy as np
import matplotlib
import scipy
import tqdm
import sklearn
import plotly
import pyAudioAnalysis

import time

from pyAudioAnalysis import audioTrainTest as aT, audioBasicIO

it = 10

for i in range(it):
     record("tralala.wav", 3.1)
     start= time.time()
     stress = (aT.file_classification("tralala.wav", "Model_Fear_gradientboosting", "gradientboosting")[1][0])*100
     print(f"niveau de stress : {int(stress)}%")
     stress = (aT.file_classification("tralala.wav", "Model_Fear_SVM", "svm")[1][0])*100
     print(f"niveau de stress : {int(stress)}%")
     stress = (aT.file_classification("tralala.wav", "Model_Fear_extratrees", "extratrees")[1][0])*100
     print(f"niveau de stress : {int(stress)}%")
     print(f"temps de calcul: {time.time()-start}")


