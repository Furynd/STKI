# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:32:04 2018

@author: User
"""

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
stem_factory = StemmerFactory()
stemmer = stem_factory.create_stemmer()

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
remo_factory = StopWordRemoverFactory()
sword_remover = remo_factory.create_stop_word_remover()

from xml.dom import minidom

def stem_rem(file):
    a = stemmer.stem(file)
    a = sword_remover.remove(a)
    return a

def xml_tag_parser(xmlfile):
    xmldoc = minidom.parse(xmlfile)
    Elementholder = xmldoc.getElementsByTagName('judul')
    judul = Elementholder[0].firstChild.data
    
    Elementholder = xmldoc.getElementsByTagName('id')
    vid = Elementholder[0].firstChild.data
    
    Elementholder = xmldoc.getElementsByTagName('tanggal')
    tanggal = Elementholder[0].firstChild.data
    
    Elementholder = xmldoc.getElementsByTagName('kata_kunci')
    katakunci = Elementholder[0].firstChild.data
    
    Elementholder = xmldoc.getElementsByTagName('isi')
    isi = Elementholder[0].firstChild.data
    isi = isi.split('\n')
    paragraf = []
    for line in isi:
        if line != "" and line != "\t" and line != " ":
            paragraf.append(stem_rem(line).split(' '))
    parlist = []
    for i in range(len(paragraf)):
        parlist.append([]);
        for word in paragraf[i]:
            if word not in parlist[i]:
                parlist[i].append(word)
    
    Elementholder = xmldoc.getElementsByTagName('link')
    link = Elementholder[0].firstChild.data
    
    return judul, vid,  tanggal, katakunci, parlist, link

judul, vid, tanggal, katakunci, par, link = xml_tag_parser('ARTIKEL XML/EKO_SA_5113100011_5113100031_5113100143/EKO_SA_07_001.xml')
