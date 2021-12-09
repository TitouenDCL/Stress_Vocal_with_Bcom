import os
import shutil
import random
from distutils.dir_util import copy_tree

"""In this function, we split de Data base (fearfull and other) into 2 data base, made
for Train and then for test, with a random choice and depending on a certain ratio"""

"""Ratio: must be in [0,1], fear_folder is the folder used for fears audios and other_folders
for the others audios, destination folder is the folder where the separation is going to be put"""
def data_split(ratio, fear_folder, other_folder, destination_folder):

    #We check if ratio is between 0 and 1
    if not (0<=ratio and ratio<=1):
        print("Ratio must be between 0 and 1")
        return

    #we check if the folders that we are going to use already exists, if so, we delete them
    if os.path.exists(destination_folder+"/X_test_fear"):
        shutil.rmtree(destination_folder+"/X_test_fear")
    if os.path.exists(destination_folder+"/X_train_fear"):
        shutil.rmtree(destination_folder+"/X_train_fear")
    if os.path.exists(destination_folder+"/X_train_other"):
        shutil.rmtree(destination_folder+"/X_train_other")
    if os.path.exists(destination_folder+"/X_test_other"):
        shutil.rmtree(destination_folder+"/X_test_other")


    #we create the 4 directories where we are going to sorte the audios
    os.makedirs(f"{destination_folder}/X_train_fear", exist_ok=True)
    os.makedirs(f"{destination_folder}/X_test_fear", exist_ok=True)

    os.makedirs(f"{destination_folder}/X_train_other", exist_ok=True)
    os.makedirs(f"{destination_folder}/X_test_other", exist_ok=True)

    #we copy the initial data bases in our directory
    copy_tree(other_folder, f"{destination_folder}/other_copy")
    copy_tree(fear_folder, f"{destination_folder}/fear_copy")

    #we count the number of audios in them
    nb_audio_fear = len(os.listdir(f"{destination_folder}/fear_copy"))
    nb_audio_other = len(os.listdir(f"{destination_folder}/other_copy"))


    #we randomly choose a number (in function of the ratio) of audios from each folder (fear and other)
    # and we put that in the folder "train", then we put the rest in the folder "test"


    for i in range(int(ratio*nb_audio_fear)):
        random_file0 = random.choice(os.listdir(f"{destination_folder}/fear_copy"))
        shutil.move(f"{destination_folder}/fear_copy/"+random_file0, f"{destination_folder}/X_train_fear")

    while len(os.listdir(f"{destination_folder}/fear_copy"))>0:
        random_file1 = random.choice(os.listdir(f"{destination_folder}/fear_copy"))
        shutil.move(f"{destination_folder}/fear_copy/"+random_file1, f"{destination_folder}/X_test_fear")

    for i in range(int(ratio*nb_audio_other)):
        random_file2 = random.choice(os.listdir(f"{destination_folder}/other_copy"))
        shutil.move(f"{destination_folder}/other_copy/"+random_file2, f"{destination_folder}/X_train_other")

    while len(os.listdir(f"{destination_folder}/other_copy"))>0:
        random_file3 = random.choice(os.listdir(f"{destination_folder}/other_copy"))
        shutil.move(f"{destination_folder}/other_copy/"+random_file3, f"{destination_folder}/X_test_other")

    nb_audio_train = len(os.listdir(f"{destination_folder}/X_Train_fear"))
    nb_audio_test = len(os.listdir(f"{destination_folder}/X_Test_fear"))
    print(f"{nb_audio_train=}")
    print(f"{nb_audio_test=}")

    #Lastly we remove the empty copied directories
    if os.path.exists(f"{destination_folder}/fear_copy"):
        shutil.rmtree(f"{destination_folder}/fear_copy")
    if os.path.exists(f"{destination_folder}/other_copy"):
        shutil.rmtree(f"{destination_folder}/other_copy")

    #then we write a readme
    file = open(f"{destination_folder}/readme", "w")
    file.write(f"This separation was made from the data bases:\n{fear_folder} for fear train and test"
               f" \n{other_folder} for other train and test ")
    file.close()

data_split(0.8, 'DataBase/Fearfull/RAVDES', 'DataBase/Neutral/RAVDES', "DataBase/Random_Train_Test")
