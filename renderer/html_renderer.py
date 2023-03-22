import os
import sys
import selenium
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

class Renderer:
    def __init__(self, exec_path="./chromedriver.exe"):
        self.driver_options = webdriver.chrome.options.Options()
        self.driver_options.add_experimental_option("detach", True)
        self.driver_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(exec_path), chrome_options=self.driver_options)
        self.inputs = {}

    def add_html(self, src: str):
        _type = ""
        if src.startswith("https://") or src.startswith("http://"):
            _type = "url"
        elif os.path.isfile(src):
            _type = "file"
            src = os.path.abspath(src)

        if len(list(self.inputs.keys())) == 0:
            self.inputs[0] = {
                "src": src,
                "type": _type
            }
        else:
            self.inputs[len(list(self.inputs.keys()))] = {
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

    def __open_new_tab(self, _id, color):
        body = self.driver.find_element(By.TAG_NAME, "body")
        self.driver.execute_script('''
            window.open('', '_blank');
        ''')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get('file://' + os.path.abspath(self.inputs[_id]['src']))
        self.driver.execute_script(f'''
            window.document.getElementsByTagName('body')[0].style.backgroundColor = '{color}';
        ''')
    
    def render(self):
        for _id in self.inputs:
            color = f"rgb({random.randint(1, 255)}, {random.randint(1, 255)}, {random.randint(1, 255)})"
            print(_id)
            self.__open_new_tab(_id, color)
        
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()




if __name__ == "__main__":
    r = Renderer()
    r.add_html("./test.html")
    r.add_html("./test copy.html")
    r.render()
