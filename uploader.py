#!/opt/homebrew/bin/python3
"""
 @Project: imageMover
 @Author: Loyio
 @Date: 2021/1/28
"""
import json
import urllib.parse


class Uploader(object):
    def __init__(self):
        self.config = {}
        self.parameters = {}
        self.path = "asdfsadf"
        self.content = "asdfsafas"
        self.getConfig()
        self.setRequestParameters(self.path, self.content)
        print(self.parameters)
        self.showConfig()

    def getConfig(self):
        with open('conf.json', 'r') as f:
            self.config = json.loads(f.read())

    def showConfig(self):
        print(self.config)

    def setRequestParameters(self, path, bas64content):
        self.parameters.update(branch=self.config["Branch"])
        self.parameters.update(path=urllib.parse.quote(path))
        self.parameters.update(content=bas64content)
        self.parameters.update(message="📡 Uploaded by imageMover \n👉🎉️ Powered by "
                                       "🔗https://github.com/loyio/imageMover 🎉👈")



