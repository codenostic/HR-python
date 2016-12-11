# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 20:28:08 2016

@author: bhupeshgupta
"""

'''
HTML Parser - 
Input = Interger N and N lines of HTML code 
Output = start, end, attribute followed by tag value

'''
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            name, value = attr[0], attr[1]
            print("->", name, ">", value)
    def handle_endtag(self, tag):
        print('End :', tag)
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for attr in attrs:
            name, value = attr[0], attr[1]
            print("-> ", name, " > ", value)



# main function 
N = int(input())
html_feed = ''
for _ in range(N):
    html_feed += input() + '\n'    # concatenate the input string into Html_Code

parser = MyHTMLParser() # feed HTML_CODE to parser and done hmm. 
parser.feed(html_feed)

'''
editors solution is pretty similar to mine. with two differences 
1) rather than using name, value editor used " > ".join(map(str, attr))
2) parser.close() method is used. 
i should remember parser.close() method 

Editor's code 
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print 'Start :',tag
        for attr in attrs:
                print '->',' > '.join(map(str,attr))
    def handle_endtag(self, tag):
        print 'End   :',tag
    def handle_startendtag(self, tag, attrs):
        print 'Empty :',tag
        for attr in attrs:
                print '->',' > '.join(map(str,attr))

html = ""
for i in range(int(raw_input())):
    html += raw_input()
                    
                
parser = MyHTMLParser()
parser.feed(html)
parser.close()


'''