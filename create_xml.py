##
# coding:utf-8
##

import os
from xml.etree import ElementTree
from xml.dom import minidom
from collections import namedtuple

IMAGE_SIZE = namedtuple('IMAGE_SIZE', ('width', 'height', 'depth'))
LABEL = namedtuple('LABEL',('name','pose','truncated','difficult','bndbox'))

def prettify(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_pascalVOC(in_dir_name,in_file_name, img_size,labels,output_file_name):

    top = ElementTree.Element('annotation')

    folder = ElementTree.SubElement(top, 'folder')
    folder.text = str(in_dir_name)

    filename = ElementTree.SubElement(top, 'filename')
    filename.text = str(in_file_name)

    source = ElementTree.SubElement(top, 'source')
    owner = ElementTree.SubElement(top, 'owner')

    size_s = ElementTree.SubElement(top, 'size')
    w = ElementTree.SubElement(size_s, 'width')
    w.text = str(img_size.width)
    h = ElementTree.SubElement(size_s, 'height')
    h.text = str(img_size.height)
    d = ElementTree.SubElement(size_s, 'depth')
    d.text = str(img_size.depth)

    seg = ElementTree.SubElement(top, 'segmented')
    seg.text = str(0)

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
    with open(output_file_name,'w') as fp:
        fp.write(elm)

def main():
    print('create xml')

    labels = []
    for i in range(10):
        labels.append(LABEL('car','Unspecified',0,0,[10,20,20,30]))

    img_size = IMAGE_SIZE(640,480,3)
    create_pascalVOC('input_dir', 'test.xml', img_size, labels,'output.xml')

if __name__ == '__main__':
    main()