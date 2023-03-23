import os
import sys
import random
import base64
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Renderer:
    def __init__(self, exec_path="./chromedriver.exe"):
        """
        creates a renderer object which can be used as a sticker generator
        """
        self.driver_options = webdriver.chrome.options.Options()
        self.driver_options.add_experimental_option("detach", True)
        self.driver_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(exec_path), chrome_options=self.driver_options)
        self.inputs = {}

    def add_html(self, src: str):
        """
        adds a html file / url which can be used as a source for creating stickers
        """

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

    def __open_new_tab(self, _id, color, folder_name):
        body = self.driver.find_element(By.TAG_NAME, "body")
        self.driver.execute_script('''
            window.open('', '_blank');
        ''')
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get('file://' + os.path.abspath(self.inputs[_id]['src']))
        self.driver.execute_script(f'''
            window.document.getElementsByTagName('body')[0].style.backgroundColor = '{color}';
        ''')
        print(str(_id) + self.inputs[_id]["src"])
        file_name = f'{str(_id) + self.inputs[_id]["src"]}.png'.replace("/", "_").replace("\\", "").replace(":","")
        print(file_name)
        self.driver.get_screenshot_as_file(file_name)
    
    def render(self):
        """
        renders the images with a generated id and returns it which can be used to get the sticker
        """

        color = f"rgb({random.randint(1, 255)}, {random.randint(1, 255)}, {random.randint(1, 255)})"
        __id = base64.b64encode(f'{time.time()}'.encode("utf8"))
        
        os.mkdir(__id)
        os.chdir(__id)
        folder_name = base64.b64encode(f'{str(time.time())}'.encode("utf8")).decode("utf8")
        for _id in self.inputs:
            print(_id)
            self.__open_new_tab(_id, color, folder_name)
        os.chdir("..")
        
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        return __id




if __name__ == "__main__":
    r = Renderer()
    r.add_html("./test.html")
    r.add_html("./test copy.html")
    r.render()
