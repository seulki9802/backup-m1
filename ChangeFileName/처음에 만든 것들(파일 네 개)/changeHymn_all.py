import os
import unicodedata
from hanspell import spell_checker


dir = os.path.join(os.getcwd(), "Libraries", "찬송가 (전체 화면)") #변경할 파일들이 담긴 폴더
ls = os.listdir(dir) #변경할 파일들

for i in ls:
    nowFileName = i

    newFileName = unicodedata.normalize("NFC", nowFileName) #파일명 자음모음 분리현상 해결
    newFileName = newFileName[:-8] #(전체).pro 날리기
    newFileName = spell_checker.check(newFileName).checked #맞춤법 검사

    if newFileName[3] != " ": #숫자뒤에 띄어쓰기가 안 된 경우
        newFileName = newFileName[:3] + " " + newFileName[3:]

    newFileName = "찬송가 " + newFileName[:3] + "." + newFileName[3:] + ".pro" #형식 ex)찬송가 001. 만원의 근원 하나님.pro

    nowDir = os.path.join(dir, nowFileName)
    newDir = os.path.join(dir, newFileName)

    os.rename(nowDir, newDir)
