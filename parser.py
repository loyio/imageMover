#!/opt/homebrew/bin/python3
"""
 @Project: imageMover
 @Author: Loyio
 @Date: 2021/1/28
"""
import re


class Parser(object):
    def __init__(self, file_path):
        self.filePath = file_path
        self.imageTextList = []
        self.readDocToImageList()
        self.__imageLinkList = []
        self.linesToImageList()

    def readDocToImageList(self):
        num = 0
        with open(self.filePath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                num += 1
                if self.boolImageText(line):
                    self.imageTextList.append([num, line])

    def boolImageText(self, line):
        return re.match(r".*!\[.*\]\(.*\)", line)

    def getImageLink(self, text):
        return re.findall(r".*!\[.*\]\((.+?)\)", text)

    def linesToImageList(self):
        for i in self.imageTextList:
            image_link_list = self.getImageLink(i[1])
            for link in image_link_list:
                self.__imageLinkList.append([i[0], link])

    def get_imageLinkList(self):
        return self.__imageLinkList
