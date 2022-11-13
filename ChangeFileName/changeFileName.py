import os
import unicodedata
from hanspell import spell_checker

class changeFileName:
    def __init__(self, folder):
        self.dir = os.path.join(os.getcwd(), "Libraries", folder)

    def deleteStr(self, strList):
        print(self.dir, " deleteStr...")
        self.ls = os.listdir(self.dir)

        for i in self.ls:
            self.nowFileName = i

            self.newFileName = unicodedata.normalize("NFC", self.nowFileName) #깨진 문자 복구

            for str in strList: #특정 문자 제거
                self.newFileName = self.newFileName.replace(str, "")

            self.changeFileName()

    def deleteNum(self):
        print(self.dir, " deleteNum...")
        self.ls = os.listdir(self.dir)

        for i in self.ls:
            self.nowFileName = i
            self.newFileName = "".join([k for k in self.nowFileName if not k.isdigit()])

            self.changeFileName()

    def spellCheck(self): #strList = [] 형식
        print(self.dir, " spellCheck...")
        self.ls = os.listdir(self.dir)

        for i in self.ls:
            self.nowFileName = i

            self.newFileName = unicodedata.normalize("NFC", self.nowFileName) #깨진 문자 복구
            self.newFileName = self.newFileName.replace(".pro", "") #.pro 잠깐 삭제
            
            self.newFileName = spell_checker.check(self.newFileName).checked #맞춤법 검사

            self.newFileName.strip() #양쪽 공백 제거
            self.newFileName += ".pro" #.pro 다시 붙이기

            self.changeFileName()
            

    def hymnFormat(self):
        print(self.dir, " hymnFormat...")
        self.ls = os.listdir(self.dir)

        for i in self.ls:
            self.nowFileName = i

            self.newFileName = unicodedata.normalize("NFC", self.nowFileName) #깨진 문자 복구
            self.newFileName = self.newFileName.replace(".pro", "") #.pro 잠깐 삭제

            #숫자 뒤에 띄어쓰기가 안 된 경우
            self.newFileName = self.newFileName[:3] + " " + self.newFileName[3:] if self.newFileName[3] != " " else self.newFileName
            
            #형식 ex)찬송가 001. 만원의 근원 하나님.pro
            self.newFileName = "찬송가 " + self.newFileName[:3] + "." + self.newFileName[3:] + ".pro"

            self.changeFileName()

    def changeFileName(self):
        nowDir = os.path.join(self.dir, self.nowFileName)
        newDir = os.path.join(self.dir, self.newFileName)

        os.rename(nowDir, newDir)

hymn_2line = changeFileName("찬송가 (두줄)")
hymn_2line.spellCheck()
hymn_2line.hymnFormat()

hymn_all = changeFileName("찬송가 (전체 화면)")
hymn_all.deleteStr(["(전체)"])
hymn_all.spellCheck()
hymn_all.hymnFormat()

ccm_2line = changeFileName("CCM (두줄)")
ccm_2line.deleteStr(["두줄", "두 줄", "자막", "_", "-"])
ccm_2line.deleteNum()
ccm_2line.spellCheck()

ccm_all = changeFileName("CCM (전체화면)")
ccm_all.deleteStr(["자막", "_", "-"])
ccm_all.deleteNum()
ccm_all.spellCheck()


