##
# coding:utf-8
##

import os
import subprocess

input_dir = '/home/wakaba/mscoco'
input_anno = '/home/wakaba/mscoco/annotations/instances_train2014.json'
input_img_dir = '/home/wakaba/mscoco/images/train2014'

output_dir = './output'
main_output_dir = 'VOCdevkit'
sub_output_dir = 'VOC2007'
annotations_dir = 'Annotations'
ImageSet_dir = 'ImageSets'
ImageSet_Layout = 'Layout'
ImageSet_Main = 'Main'
JPEGImages_dir = 'JPEGImages'


def main():
    print('mscoco_to_voc')

    sub_path = '{}/{}/{}'.format(output_dir, main_output_dir, sub_output_dir)
    if not os.path.isdir(output_dir):
        os.makedirs(sub_path)
        #os.mkdir('{}/{}'.format(sub_path,annotations_dir))
        os.mkdir('{}/{}'.format(sub_path,ImageSet_dir))
        os.mkdir('{}/{}/{}'.format(sub_path, ImageSet_dir, ImageSet_Layout))
        os.mkdir('{}/{}/{}'.format(sub_path, ImageSet_dir, ImageSet_Main))
        os.mkdir('{}/{}'.format(sub_path,JPEGImages_dir))
    else:
        print('Error main : output_dir is exist.')
        exit()

    subprocess.check_call(['python3', 'mscoco/mscoco.py', input_anno, input_img_dir, '{}/{}'.format(sub_path,annotations_dir)])

if __name__ == '__main__':
    main()