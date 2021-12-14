import os
import shutil
import random
from distutils.dir_util import copy_tree

"""In this function, we split de Data base (fearfull and other) into 2 data base, made
for Train and then for test, we isolate one actor for the tests"""

"""Actor must be a 2 digit number between 01 and 24 written as a string, example : '08' """

def data_split_actor(actor, fear_folder, other_folder, destination_folder):
    """Actor must be a 2 digit number between 01 and 24 written as a string, example : '08' """

    path_test_fear = f"{destination_folder}/test/fear"
    path_train_fear = f"{destination_folder}/train/fear"
    path_test_other = f"{destination_folder}/test/other"
    path_train_other = f"{destination_folder}/train/other"
    # we check if the folders that we are going to use already exists, if so, we delete them
    if os.path.exists(path_test_fear):
        shutil.rmtree(path_test_fear)
    if os.path.exists(path_train_fear):
        shutil.rmtree(path_train_fear)
    if os.path.exists(path_train_other):
        shutil.rmtree(path_train_other)
    if os.path.exists(path_test_other):
        shutil.rmtree(path_test_other)

    # we create the 4 directories where we are going to sorte the audios
    os.makedirs(path_train_fear, exist_ok=True)
    os.makedirs(path_test_fear, exist_ok=True)

    os.makedirs(path_train_other, exist_ok=True)
    os.makedirs(path_test_other, exist_ok=True)

    # we copy the initial data bases in our directory
    copy_tree(other_folder, f"{destination_folder}/other_copy")
    copy_tree(fear_folder, f"{destination_folder}/fear_copy")

    # we select all the audio from the selected actor and put it in test folders,
    # we put the others in train folders
    for filename in os.listdir(f"{destination_folder}/fear_copy"):
        if filename.split("-")[-1] == f"{actor}.wav":
            shutil.move(f"{destination_folder}/fear_copy/{filename}", path_test_fear)
        else:
            shutil.move(f"{destination_folder}/fear_copy/{filename}", path_train_fear)

    for filename in os.listdir(f"{destination_folder}/other_copy"):
        if filename.split("-")[-1] == f"{actor}.wav":
            shutil.move(f"{destination_folder}/other_copy/{filename}", path_test_other)
        else:
            shutil.move(f"{destination_folder}/other_copy/{filename}", path_train_other)

    nb_audio_train = len(os.listdir(path_train_fear))
    nb_audio_test = len(os.listdir(path_test_fear))

    # Lastly we remove the empty copied directories
    if os.path.exists(f"{destination_folder}/fear_copy"):
        shutil.rmtree(f"{destination_folder}/fear_copy")
    if os.path.exists(f"{destination_folder}/other_copy"):
        shutil.rmtree(f"{destination_folder}/other_copy")

    # then we write a readme
    file = open(f"{destination_folder}/readme", "w")
    file.write(f"This separation was made from the data bases:\n{fear_folder} for fear train and actor {actor} for test"
               f" \n{other_folder} for other train and actor {actor} for test")
    file.close()


