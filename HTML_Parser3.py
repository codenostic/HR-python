# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:27:18 2016

@author: bhupeshgupta
"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag, attrs):
        print(tag)
        for attr in attrs:
            print('-> '+" > ".join(map(str,attr)))
    

html = ''
N = int(input())
for _ in range(N):
    html += input() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

'''
this is exactly similar to editor may be a bit better. 
'''