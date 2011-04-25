from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
from lxml import etree

class Tisztitas(object):

        def __init__(self, url):
                self.url = url

        def megnyit(self):
                return urlopen(self.url)

        def beolvasKodolva(self):
                i = self.megnyit().read()
                return BeautifulSoup(i.decode('latin-1'))
                


class JozsefAttila(object):

        def __init__(self, url):
                self.url = Tisztitas(url).beolvasKodolva()
                self.eredmeny = []

     
        def cimekListaja(self):
                return self.url.findAll('a', attrs={'name' : True})
        
        def cimekSzoveggel(self):
                cimek = self.cimekListaja()
                cimek.reverse()
                print cimek.pop()
                for i in self.url.findAll('p'):
                        if i.find('a'):
                                print 'cim', i
                                cimek.pop()
                        else:
                                print 'szoveg', i


                                     
class EredmenyekKinyerese(object):
        
        def __init__(self, url):
                self.url = Tisztitas(url).beolvasKodolva()
        
        def cimekListaja(self):
                return self.url.findAll('a', attrs={'name' : True})
        
        def cimekSzoveggel(self):
                cimek = self.cimekListaja()
                cimek.reverse()
                                
                versek = etree.Element("versek")
                                
                first = cimek.pop()
                vers = etree.SubElement(versek, 'vers')
                etree.SubElement(vers, "cim").text = first.text
                for i in self.url.findAll('p'):
                        if i.find('a', attrs={'name' : True}):
                                vers = etree.SubElement(versek, 'vers')
                                
                                etree.SubElement(vers, "cim").text = i.text
                        elif i.text != "" and 'document.write' not in i.text:
                                etree.SubElement(vers, "bekezdes").text = i.text
                print etree.tostring(versek, encoding='utf-8',  pretty_print=True)

                
