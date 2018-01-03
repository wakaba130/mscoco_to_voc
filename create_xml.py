##
# coding:utf-8
##

import os
from xml.etree import ElementTree
from xml.dom import minidom
from collections import namedtuple

LABEL = namedtuple('LABEL',('name','pose','truncated','difficult','bndbox'))

def prettify(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_pascalVOC(labels,file_name):

    top = ElementTree.Element('annotation')

    for label in labels:
        object = ElementTree.SubElement(top, 'object')

        name = ElementTree.SubElement(object, 'name')
        name.text = str(label.name)

        pose = ElementTree.SubElement(object, 'pose')
        pose.text = str(label.pose)

        truncated = ElementTree.SubElement(object, 'truncated')
        truncated.text = str(label.truncated)

        bbox = ElementTree.SubElement(object, 'bndbox')
        xmin = ElementTree.SubElement(bbox, 'xmin')
        xmin.text = str(int(label.bndbox[0]))
        ymin = ElementTree.SubElement(bbox, 'ymin')
        ymin.text = str(int(label.bndbox[1]))
        xmax = ElementTree.SubElement(bbox, 'xmax')
        xmax.text = str(int(label.bndbox[0] + label.bndbox[2]))
        ymax = ElementTree.SubElement(bbox, 'ymax')
        ymax.text = str(int(label.bndbox[0] + label.bndbox[3]))

    elm = prettify(top)
    with open(file_name,'w') as fp:
        fp.write(elm)

def main():
    print('create xml')

    labels = []
    for i in range(10):
        labels.append(LABEL('car','None',0,0,[10,20,20,30]))

    create_pascalVOC(labels,'output.xml')

if __name__ == '__main__':
    main()