import shutil,os

def remover(temp_path):
    print("REMOVER START")
    ## temporary storage 삭제
    shutil.rmtree(temp_path)

    ## temporary storage 빈 디렉토리 생성
    os.makedirs(temp_path)