from sqlalchemy import Integer, Column, create_engine,String, TIMESTAMP
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None

from src import config
 
import hashlib

 
class Vaga(Base):
    
    __tablename__ = 'vagas'

    id = Column(Integer, primary_key=True)
    uid = Column(String)
    cargo = Column(String)
    link_Vaga = Column(String)
    texto_vaga = Column(String)
    texto_busca = Column(String)
    data_criacao = Column( TIMESTAMP,server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
                          
    def __init__(self, cargo, link_Vaga, texto_vaga, texto_busca):
        
        self.cargo = cargo
        self.link_Vaga = link_Vaga
        self.texto_vaga = texto_vaga
        self.texto_busca = texto_busca
        self.uid         = hashlib.md5(link_Vaga)
    