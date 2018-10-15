#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
from smallsmilhandler import SmallSMILHandler

if __name__ == "__main__":


    parser = make_parser()
    cHandler = SmallSMILHandler()

    parser.setContentHandler(cHandler)
    fichero = sys.argv[1]
    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
    parser.parse(open(fichero))

    misdatos = cHandler.get_tags()

    for etiqueta in misdatos:
        salida = ""
        elemento = etiqueta.items() #es un diccionario
    for datos in misdatos:
    	print(elemento)
    	for etiqueta in datos:
    		for atributo, valor in datos[etiqueta].items():
    			salida = salida + etiqueta + " \ " + atributo + '="' + valor + '"\ '
    	print(salida)
    	salida = ""
