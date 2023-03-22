import os
import sys
import selenium

class Renderer:
    def __init__(self, exec_path="./chromedriver.exe"):
        self.driver = selenium.webdriver.Chrome(executable_path=os.path.abspath(exec_path))

    def add_html(self, src: str):
        if src.startswith("https://") or src.startswith("http://"):
            self.type = "url"
        elif os.path.isfile(src):
            self.type = "file"
        
    def from_string(self, markup: str):
        self.type = "markup"
        self.value = markup
    