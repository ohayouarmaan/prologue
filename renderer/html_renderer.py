import os
import sys
import selenium

class Renderer:
    def __init__(self, exec_path="./chromedriver.exe"):
        self.driver_options = selenium.webdriver.chrome.options.Options()
        self.driver_options.add_experimental_option("detach", True)
        self.driver = selenium.webdriver.Chrome(executable_path=os.path.abspath(exec_path), chrome_options=self.driver_options)
        self.inputs = {}

    def add_html(self, src: str):
        _type = ""
        if src.startswith("https://") or src.startswith("http://"):
            _type = "url"
        elif os.path.isfile(src):
            _type = "file"

        if len(list(self.inputs.keys())) == 0:
            self.inputs[0] = {
                "src": src,
                "type": _type
            }
        else:
            self.inputs[len(list(self.inputs.keys())) - 1] = {
                "src": src,
                "type": _type
            }
        
    def from_string(self, markup: str):
        _type = "markup"
        self.value = markup

        if len(list(self.inputs.keys())) == 0:
            self.inputs[0] = {
                "src": markup,
                "type": _type
            }
        else:
            self.inputs[len(list(self.inputs.keys())) - 1] = {
                "src": markup,
                "type": _type
            }
    
    def render(self):
        if self.type == "url":
            self.driver
