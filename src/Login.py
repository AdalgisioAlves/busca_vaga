from src import config
from src import configureBrowser
from selenium.webdriver.common.keys import Keys
from src import HtmlToArray


class Login(configureBrowser.ConfigBrowser):
    
    def __init__(self):
        self.usuario = config.conf["usuario"]
        self.senha = config.conf["senha"]
        super().__init__()
 
    def login(self, inputUsuario, inputSenha,btnLogar):
        br = self.browser  
        
        usuario = br.find_element_by_id(inputUsuario)
        usuario.send_keys(self.usuario)
        
        senha = br.find_element_by_id(inputSenha)
        senha.send_keys(self.senha)
        
        btn = br.find_element_by_xpath(btnLogar)
        br.implicitly_wait(2)
        btn.click()
        
        
        return br        
            
        
        
        
    