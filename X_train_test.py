import os
import shutil


def data_split(coef, fear_folder, other_folder):
    if os.path.exists("DataBase/Random_Train_Test/X_test_fear"):
        shutil.rmtree("DataBase/Random_Train_Test/X_test_fear")
    if os.path.exists("DataBase/Random_Train_Test/X_train_fear"):
        shutil.rmtree("DataBase/Random_Train_Test/X_train_fear")
    if os.path.exists("DataBase/Random_Train_Test/X_train_other"):
        shutil.rmtree("DataBase/Random_Train_Test/X_train_other")
    if os.path.exists("DataBase/Random_Train_Test/X_test_other"):
        shutil.rmtree("DataBase/Random_Train_Test/X_test_other")

    print("ok0")
    os.makedirs("X_train_fear", exist_ok=True)
    os.makedirs("X_test_fear", exist_ok=True)

    os.makedirs("X_train_other", exist_ok=True)
    os.makedirs("X_test_other", exist_ok=True)

    print("ok1")

    audios_fear = os.listdir('X_train_fear').__sizeof__()
    #    audios_other = os.listdir(other_folder).__sizeof__()
    print("ok2")


data_split(0, 'DataBase/Fearfull/RAVDES', 'DataBase/Neutral/RAVDES')
