#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys

class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.width = ""
        self.heigth = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.misdatos = []

    def startElement(self, etiqueta, attrs):

        if etiqueta == 'root-layout':
            rootlayout = {'rootlayout': ({'width': attrs.get('width', ""),
                                          'height': attrs.get('height', ""),
                                          'background-color': attrs.get('background-color')})}
            self.misdatos.append(rootlayout)
        elif etiqueta == 'region':
            region = {'region': ({'id': attrs.get('id', ""),
                                  'top': attrs.get('top', ""),
                                  'bottom': attrs.get('bottom', ""),
                                  'left': attrs.get('left', ""),
                                  'right': attrs.get('right', "")})}
            self.misdatos.append(region)
        elif etiqueta == 'img':
            img = {'img': ({'src': attrs.get('src', ""),
                            'region': attrs.get('region', ""),
                            'begin': attrs.get('begin', ""),
                            'dur': attrs.get('dur', "")})}
            self.misdatos.append(img)
        elif etiqueta == 'audio':
            audio = {'audio': ({'src': attrs.get('src', ""),
                                'abegin': attrs.get('begin', ""),
                                'dur': attrs.get('dur', "")})}
            self.misdatos.append(audio)
        elif etiqueta == 'textstream':
            textstream = {'textstream': ({'src': attrs.get('src', "")})}
            self.misdatos.append(textstream)

    def get_tags(self):
        return self.misdatos

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python3 smallsmilhandler.py file.smil")
    parser.parse(open(fichero))
    misdatos = cHandler.get_tags()
    for line in misdatos:
        print(line)
        print("\n")
