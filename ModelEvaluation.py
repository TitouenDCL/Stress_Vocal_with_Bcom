import numpy as np
import matplotlib
import scipy
import tqdm
import sklearn
import plotly
import pyAudioAnalysis
from pyAudioAnalysis.audioTrainTest import random_split_features
from sklearn.model_selection import train_test_split
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import MidTermFeatures
import matplotlib.pyplot as plt
import train_test

from pyAudioAnalysis import audioTrainTest as aT
'''
cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders(["DataBase/Random_Train_Test/test\\fear",
                                                                           "DataBase/Random_Train_Test/test\\other"],
                                                                          "Model_Fear_SVM",
                                                                          "svm",
                                                                          "fear")

cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders(["DataBase/Random_Train_Test/test\\fear",
                                                                           "DataBase/Random_Train_Test/test\\other"],
                                                                          "Model_Fear_randomforest",
                                                                          "randomforest",
                                                                          "fear")


cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders(["DataBase/Random_Train_Test/test\\fear",
                                                                           "DataBase/Random_Train_Test/test\\other"],
                                                                          "Model_Fear_gradientboosting",
                                                                          "gradientboosting",
                                                                          "fear")


cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders(["DataBase/Random_Train_Test/test\\fear",
                                                                           "DataBase/Random_Train_Test/test\\other"],
                                                                          "Model_Fear_extratrees",
                                                                          "extratrees",
                                                                          "fear")

cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders(["DataBase/Random_Train_Test_Actors/test\\fear",
                                                                           "DataBase/Random_Train_Test_Actors/test\\other"],
                                                                          "Model_Fear_gradientboosting_Actors",
                                                                          "gradientboosting",
                                                                          "fear")
'''
for i in range(11, 20):
    cm, thr_prre, pre, rec, thr_roc, fpr, tpr = aT.evaluate_model_for_folders(
        [f"DataBase/Random_Train_Test_Actors_{i}/test\\fear",
         f"DataBase/Random_Train_Test_Actors_{i}/test\\other"],
        f"Model_Fear_gradientboosting_Actors_{i}",
        "gradientboosting",
        "fear")
