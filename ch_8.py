#! /usr/bin/python3

from lxml import etree

tree18 =  etree.parse("data/TEI/sonnet18.xml")
tree17 =  etree.parse("data/TEI/sonnet17.xml")

root = tree17.getroot()

for x in tree17.iterfind("//l"):
    print(x.tag)





