import shutil
import os

def remover(temp_storage_path: str) -> None:
    print("remover 시작")
    shutil.rmtree(temp_storage_path)
    os.makedirs(temp_storage_path)