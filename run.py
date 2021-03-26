from src import Login
from src import HtmlToArray
 

##INCIALIZANDO RASPADOR
 
objLogin = Login.Login()
 
usuario = {"find_element_by_id", "username"}
senha   = {"find_element_by_id", "password"}
botao   = {"find_element_by_css_selector", "btn__primary"}

 
objLogin.login("username","password","/html/body/div/main/div[2]/div[1]/form/div[3]/button")

HtmlToArray.htmlToArray.scrapLinkedin(objLogin.browser)

print('Fim')





