# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:54:00 2019

@author: 20004411
"""
#encoding: utf-8
from yattag import Doc,indent
import csv
import re
import unidecode
import os
from os import listdir
from os.path import isfile, join     

def geraCabecalhoYazaki():  
    file = open('template/cabecalhoYazaki.html','r',encoding = "utf-8")
    data = file.read() 
    return data

def geraHtmlHeader():  
    file = open('template/header.html','r',encoding = "utf-8")
    data = file.read() 
    return data



def gera_index(paginas,path):
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        doc.asis(geraHtmlHeader())
    file = open(path+'index.html','w',encoding = "utf-8")             
    with tag('body',style="margin:0px;padding:0px;overflow:hidden"):
        doc.asis(geraCabecalhoYazaki())
        with tag('div', klass="list-group"):
            for titulo,pagina in paginas:
                with tag('a' ,href='./'+formatar(pagina),klass="btn btn-primary"):
                    text(titulo)
    webpage=indent(doc.getvalue()) 
    print(webpage)
    file.write(webpage)
    file.close()
    
def formatar(string):
    formatada = string.replace(" ", "_")
    re.sub('[^A-Za-z0-9]+', '', formatada)
    formatada = unidecode.unidecode(formatada)
    return formatada
    
    


print("Iniciando...")
path = "C:/wamp64/www/" 
moto = ["Formulários Moto","./formularios/moto/index.html"]
manutencao = ["Formulários Manutenção","./formularios/manutencao/index.html"]
ti = ["Formulários T.I","./formularios/ti/gerenciamento.html"]
seguranca = ["Formulários Segurança","./formularios/seguranca/index.html"]
rasp = ["Update Raspberry Pi Screen","./rasp/atualizar.html"]
htmls=[moto,manutencao,ti,seguranca,rasp,rasp2]
#geraCabecalhoYazaki()
gera_index(htmls,path)
print("pagina Gerada")




