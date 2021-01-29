#!/opt/homebrew/bin/python3
"""
 @Project: imageMover
 @Author: Loyio
 @Date: 2021/1/28
"""
import sys
from uploader import *
from parser import *
if __name__ == '__main__':
    if (len(sys.argv) < 2) or not(sys.argv[1][-3:] == ".md"):
        print("❗️ Please append a markdown file path ❗️")
    else:
        markdown_file_path = sys.argv[1]
        parser = Parser(markdown_file_path)
        print(parser.get_imageLinkList())
        uploader = Uploader()
        uploader.getImageFromUrl(parser.get_imageLinkList()[0][1])
