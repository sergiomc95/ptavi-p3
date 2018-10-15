#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import json
from smallsmilhandler import SmallSMILHandler

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    try:
	       fichero = sys.argv[1]
    except IndexError:
		   sys.exit("Usage: python3 karaoke.py file.smil")

    parser.parse(open(fichero))
    misdatos = cHandler.get_tags()
    salida = ""
    for datos in misdatos:
        for etiqueta in datos:

                for atributo, valor in datos[etiqueta].items():

                    salida = salida + '\t' + atributo + ' = "' + valor + '"\t'
        print(etiqueta + salida)
        salida = ""
    json.dump(misdatos, open('karaoke.json', 'w'))
