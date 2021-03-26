from selenium import webdriver
from src    import config

class ConfigBrowser():
    def __init__(self,url = None):
        self.url =  url if url != None else config.conf["url"] 
        self.browser        =   webdriver.Firefox(executable_path= r'./driver/geckodriver.exe')
        self.browser.get(self.url)
   
    def fechar(br):
        br.close()
        print('Fim')
    
    
        
