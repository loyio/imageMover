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
        self.imageTextList = {}
        self.readDocToImageList()
        pass

    def readDocToImageList(self):
        num = 1
        with open(self.filePath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                num += 1
                print(str(num)+line)
                print(self.boolImageText(line))

    def boolImageText(self, line):
        return re.match("\!\[*\]\(*\)", line)
