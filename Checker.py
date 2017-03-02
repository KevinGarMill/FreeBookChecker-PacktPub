#!/usr/bin/env python
#-*- coding: utf-8 -*-
#vim: set fileencoding=utf8 :

'''
Cliente web para https://www.packtpub.com/packt/offers/free-learning
Su objetivo es Informar al usuario del nuevo libro gratuito

@autor: kevingarmill@gmail.com
'''
import urllib2


class Checker(object):
    def get_web(self, page):
        f = urllib2.urlopen(page)
        html = f.read()
        f.close
        print html


    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/free-learning')
        # get title book
        # print title book


if __name__ == "__main__":
    checker = Checker()
    checker.main()
