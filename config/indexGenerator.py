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
    file = open('lib/header.html','r',encoding = "utf-8")
    data = file.read() 
    return data



def gera_index(paginas,path):
    doc, tag, text = Doc().tagtext()
    file = open(path+'index.html','w',encoding = "utf-8")  
    with tag('html'):
        with tag('head'):
            doc.stag('meta', charset='UTF-8')
            doc.stag('link', rel="stylesheet", href="/repo/bootstrap.min.css")
            doc.stag('link', rel="stylesheet", href="/repo/jquery.min.js")
            doc.stag('link', rel="stylesheet", href="/repo/bootstrap.min.js")
            doc.stag('link', rel="stylesheet", href="/repo/carousel.css")
        with tag('body',style="margin:0px;padding:0px;overflow:hidden"):
            doc.asis(geraCabecalhoYazaki())
            with tag('div', klass="list-group"):
                for titulo,pagina in paginas:
                    with tag('a' ,href='./'+formatar(pagina),klass="btn btn-primary"):
                        text(titulo)
    webpage=indent(doc.getvalue()) 
    file.write(webpage)
    file.close()
    
def formatar(string):
    formatada = string.replace(" ", "_")
    re.sub('[^A-Za-z0-9]+', '', formatada)
    formatada = unidecode.unidecode(formatada)
    return formatada
    
    



path = "C:/wamp64/www/" 
htmls=[["Formulários Moto","./formularios/moto/index.html"]]
geraCabecalhoYazaki()
gera_index(htmls,path)




