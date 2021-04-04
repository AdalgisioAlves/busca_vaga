from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time as time
from src import db
import sys
import os
#os.environ['MOZ_HEADLESS'] = '1'


class htmlToArray():
    
    def scrapLinkedin(br):
        
        busca_por = 'Analista de sistemas'
        br.get('https://www.linkedin.com/jobs/search/?keywords='+busca_por+'&location=Brasil')
        time.sleep(8)
        n_paginas = len(br.find_elements_by_class_name("artdeco-pagination__pages")[0].find_elements(By.TAG_NAME,"button") )
        try:
            p = 0
            proxima_pagina = 0
            while n_paginas > p:
                if p > 0:
                    
                    proxima_pagina = proxima_pagina + 25
                    br.get('https://www.linkedin.com/jobs/search/?keywords='+busca_por+'&location=Brasil&&start='+str(proxima_pagina) )
                    time.sleep(15)

                    
                jobs_ul = br.find_elements_by_class_name("jobs-search-results__list-item") 
                    
                rs = db.DB()
                for li in jobs_ul:                
                                    
                        a       = li.find_elements(By.TAG_NAME,"a")   
                        if len(a) >2:
                            
                            a_link          = a[0].get_attribute('href').split("/")
                            cargo           = a[1].text
                            texto_vaga      = li.text                            
                            id_vaga         = a_link[5]
                            n = 0 
                            link = ""
                            for val in a_link:
                                if n <= 5:
                                    link += val+"/"
                                    n = n + 1
                            
                            data  = {
                                "cargo" : cargo,
                                "link_vaga" : link, 
                                "desc_vaga" : texto_vaga, 
                                "texto_busca" : busca_por,
                                "id_vaga": id_vaga
                                }
                            salvar  = rs.salvar(data) 
                            if salvar == '0':
                                print('erro ao inserir registro')
                            if salvar == '01':
                                print('Registro já existe no banco')
                            else:
                                print('Registro inserido ',salvar)
                p = p + 1
            br.close()
        
                
        except NoSuchElementException :
            print('Erro Pagina nãoo carregada corretamento')
                
            
            
       
     
        