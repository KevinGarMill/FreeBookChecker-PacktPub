#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

'''
Cliente web para https://www.packtpub.com/packt/offers/free-learning
Su objetivo es Informar al usuario del nuevo libro gratuito

@autor: kevingarmill@gmail.com
'''
import urllib2
from bs4 import BeautifulSoup


class Checker(object):
    def get_web(self, page):
        f = urllib2.urlopen(page)
        html = f.read()
        f.close
        return html

    def search_title(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        element = soup.find_all("div", "dotd-title")
        title = element[0].find("h2")
        if title:
            title = title.text
        return title.strip()

    def main(self):
        web = self.get_web('https://www.packtpub.com/packt/offers/free-learning')
        title = self.search_title(web)
        print title


if __name__ == "__main__":
    checker = Checker()
    checker.main()
