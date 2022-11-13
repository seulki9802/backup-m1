import os
import unicodedata
from hanspell import spell_checker


dir = os.path.join(os.getcwd(), "Libraries", "CCM (전체화면)") #변경할 파일들이 담긴 폴더
ls = os.listdir(dir) #변경할 파일들

for i in ls:
    nowFileName = i

    newFileName = unicodedata.normalize("NFC", nowFileName) #파일명 자음모음 분리현상 해결
    newFileName = newFileName.strip(".pro").strip("두줄").strip("두 줄").strip("자막") #불필요한 것 제거

    newFileName = spell_checker.check(newFileName).checked #맞춤법 검사

    newFileName = newFileName + ".pro" #.pro 다시 붙여주기

    nowDir = os.path.join(dir, nowFileName)
    newDir = os.path.join(dir, newFileName)

    os.rename(nowDir, newDir)
