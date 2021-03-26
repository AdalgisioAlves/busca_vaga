import mysql.connector
 

from src import config

class DB():
    
    def __init__(self):
        self.db_conf = mysql.connector.connect(
                        host    =   config.conf['db_host'] ,
                        user    =   config.conf['db_usuario'],
                        password    =   config.conf['db_senha'],
                        database    =   config.conf['db'],
                        port        =   config.conf['porta'],
                        )
        

    def salvar(self,values):
        try:
            valida_vaga = self.validar_vaga(values['id_vaga'])
            if valida_vaga == 0:
                            
                sql = ('INSERT INTO vagas (cargo,link_vaga,desc_vaga,texto_busca,id_vaga)'
                            "VALUES(%(cargo)s,%(link_vaga)s,%(desc_vaga)s,%(texto_busca)s,%(id_vaga)s)")            
                conn = self.db_conf.cursor()
                conn.execute(sql, values)
                id_vaga = conn.lastrowid
                conn.close()
                return id_vaga
            else:
                return '01'
             
        except  mysql.connector.Error as err:
            return '0'
        
    def fechar(self):
        self.db_conf.close()
        
        
    def update(self,query,where):
        conn = self.db_conf.cursor()

        insetrt = conn.execute(sql, where)
        conn.commit()
        conn.close()
        return insetrt.lastrowid
    
    def criar_query(self,tabela,campos,where):
       
        sql =[]                         
        for d in campos:            
            sql.append(d + "='" +data[d]+"'") 
            campo_sql = ",".join(sql)
            return  " UPDATE "+ tabela +" SET "+ campo_sql + where
        print()
        
    def validar_vaga(self, id_vaga):
        
        sql = "select id from vagas where id_vaga ='"+id_vaga+"'"
        conn = self.db_conf.cursor() 
        conn.execute(sql)
        rs      = conn.fetchall()
        conn.close()
        if len(rs) > 0:
            return 1
        else:
            return 0