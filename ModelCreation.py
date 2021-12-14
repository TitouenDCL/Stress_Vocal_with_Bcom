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
import train_test_actor
from pyAudioAnalysis import audioTrainTest as aT


#[Fs, x] = audioBasicIO.read_audio_file("DataBase/Fearfull/nicolas add/MISSING TODDLERS_ Biological mom expresses her worries - 1of3 - 3of6.mp3")

train_test.data_split(0.8, 'DataBase/Stress/RAVDES', 'DataBase/other/RAVDES', "DataBase/Random_Train_Test")

"""Dans le path des bases de données, j'ai mis \\ devant le dernier nom, dans mon cas c'est néscéssaire 
probablement parceque je suis sous windows.
Pour savoir si il faut mettre \\ ou simplement /, il faut tester la valeur de os.sep

os.sep= '/' -> mettre un path de type DataBase/Random_Train_Test/train/fear
os.sep= '\\'' ->  mettre un path de type DataBase/Random_Train_Test/train\\fear

c'est néscéssaire pour que l'évaluation du modèle se fasse correctement
"""



'''
aT.extract_features_and_train(["DataBase/Random_Train_Test/train\\fear",
                               "DataBase/Random_Train_Test/train\\other"],
                              1.0, 1.0, aT.shortTermWindow, aT.shortTermStep,
                              "svm",
                              "Model_Fear_SVM")

aT.extract_features_and_train(["DataBase/Random_Train_Test/train\\fear",
                               "DataBase/Random_Train_Test/train\\other"],
                              1.0, 1.0, aT.shortTermWindow, aT.shortTermStep,
                              "extratrees",
                              "Model_Fear_extratrees")


aT.extract_features_and_train(["DataBase/Random_Train_Test/train\\fear",
                               "DataBase/Random_Train_Test/train\\other"],
                              1.0, 1.0, aT.shortTermWindow, aT.shortTermStep,
                              "gradientboosting",
                              "Model_Fear_gradientboosting")

aT.extract_features_and_train(["DataBase/Random_Train_Test/train\\fear",
                               "DataBase/Random_Train_Test/train\\other"],
                              1.0, 1.0, aT.shortTermWindow, aT.shortTermStep,
                              "randomforest",
                              "Model_Fear_randomforest")
'''

for j in range(70, 100, 5):
    i=j/100
    print(str(f"{i}"))
    train_test.data_split(i, 'DataBase/Stress/RAVDES', 'DataBase/other/RAVDES', f"DataBase/Random_Train_Test_Coef_{i}")
    print(f"split")
    aT.extract_features_and_train([f"DataBase/Random_Train_Test_Coef_{i}/train\\fear",
                               f"DataBase/Random_Train_Test_Coef_{i}/train\\other"],
                              1.0, 1.0, aT.shortTermWindow, aT.shortTermStep,
                              "gradientboosting",
                              f"Model_Fear_gradientboosting_Coef_{i}")