from lxml import etree
import os
from os.path import join



path = 'C:/Users/Public/Documents/Real_Masters_all'
for filename in os.listdir(path):
    tree = etree.parse(join(path, filename))
    if tree.xpath("//table"):
        fout = open('C:/Users/Public/Documents/tables.txt', 'a')
        fout.write(filename + '\n')
        fout.close()
