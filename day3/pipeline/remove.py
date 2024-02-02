from settings import TEMP_PATH
import shutil, os

def remover(path):

    shutil.rmtree(path)
    os.makedirs(path)