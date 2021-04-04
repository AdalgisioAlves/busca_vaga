br.get('https://www.linkedin.com/jobs/search/?currentJobId=2447206536&geoId=106057199&keywords=php&location=Brasil')
        time.sleep(7)
        paginacao = br.find_elements_by_class_name("artdeco-pagination__pages")[0].find_elements(By.TAG_NAME,"button") 
        #paginacao.remove(0)
        pa = 0
        for btn in paginacao :
            try: 
                if pa > 0:
                    br.refresh()
                    btn.click()
                    time.sleep(8)
                
                jobs_ul = br.find_elements_by_class_name("jobs-search-results__list-item") 
                
                pa = pa + 1   
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
            except :
                print("Erro desconhecido:", sys.exc_info())
        br.close()
        return True