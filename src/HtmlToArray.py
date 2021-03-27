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
        
        
        br.get('https://www.linkedin.com/jobs/search/?currentJobId=2447206536&geoId=106057199&keywords=php&location=Brasil')
        time.sleep(8)
        n_paginas = len(br.find_elements_by_class_name("artdeco-pagination__pages")[0].find_elements(By.TAG_NAME,"button") )
        
        p = 0
        while n_paginas > p:
            if p > 0:
                br.refresh();
                time.sleep(3)
                btn = br.find_elements_by_class_name("artdeco-pagination__pages")[0].find_elements(By.TAG_NAME,"button")
                btn[p].click()
                time.sleep(10)
                
            jobs_ul = br.find_elements_by_class_name("jobs-search-results__list-item") 
                
            rs = db.DB()
            for li in jobs_ul:                
                                
                    a       = li.find_elements(By.TAG_NAME,"a")   
                    if len(a) >2:
                        
                        a_link          = a[0].get_attribute('href').split("/")
                        cargo           = a[1].text
                        texto_vaga      = li.text
                        texto_busca     = 'php'
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
                            "texto_busca" : texto_busca,
                            "id_vaga": id_vaga
                            }
                        rs.salvar(data) 
                        if rs == '0':
                            print('erro ao inserir registro')
                        if rs == '01':
                            print('Registro já existe no banco')
                        else:
                            print('Registro inserido ',rs)
            p = p + 1
                
            
            
       
     
        