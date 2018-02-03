##
# coding:utf-8
##

import os
import sys
import subprocess
from mscoco import mscoco

year = '2014'
input_dir = '/home/wakaba/mscoco2'
output_dir = '/home/wakaba/output_test_dir'

train_2014_url = 'http://images.cocodataset.org/zips/train2014.zip'
val_2014_url = 'http://images.cocodataset.org/zips/val2014.zip'

train_2017_url = 'http://images.cocodataset.org/zips/train2017.zip'
val_2017_url = 'http://images.cocodataset.org/zips/val2017.zip'

anno_2014_url = 'http://images.cocodataset.org/annotations/annotations_trainval2014.zip'
anno_2017_url = 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip'

###
annotations = 'annotations'
images = 'images'

def check_dataset(input_path):
    # check dataset dir
    if not os.path.isdir('{}'.format(input_path)):
        os.makedirs(input_path)

    # check annotation file
    if not os.path.isfile('{}/{}/instances_train{}.json'.format(input_path, annotations, year)):
        if year == '2014':
            subprocess.check_call(['wget', '-c', anno_2014_url], cwd=input_path)
        else:
            subprocess.check_call(['wget', '-c', anno_2017_url], cwd=input_path)

        subprocess.check_call(['unzip', '{}/annotations_trainval{}.zip'.format(input_path, year)],
                              cwd=input_dir)

    # check train data
    if not os.path.isdir('{}/{}/train{}'.format(input_path, images, year)):
        if not os.path.isdir('{}/{}'.format(input_path, images)):
            os.mkdir('{}/{}'.format(input_path, images))

        if year == '2014':
            subprocess.check_call(['wget', '-c', train_2014_url], cwd=input_path)
        else:
            subprocess.check_call(['wget', '-c', train_2017_url], cwd=input_path)

        subprocess.check_call(
            ['unzip', '{}/train{}.zip'.format(input_path, year)],
            cwd='{}/{}'.format(input_path, images))

    # check val data
    if not os.path.isdir('{}/{}/val{}'.format(input_path, images, year)):
        if year == '2014':
            subprocess.check_call(['wget', '-c', val_2014_url], cwd=input_path)
        else:
            subprocess.check_call(['wget', '-c', val_2017_url], cwd=input_path)

        subprocess.check_call(
            ['unzip', '{}/val{}.zip'.format(input_path, year)],
            cwd='{}/{}'.format(input_path, images))

def main():
    print('test')

    if os.path.isdir(output_dir):
        print('Error : output dir is exist.')
        sys.exit()

    check_dataset(input_dir)

    for set in ['train', 'val']:
        print('== output {} =='.format(set))
        anno = '{}/{}/instances_{}{}.json'.format(input_dir, annotations, set, year)
        img = '{}/{}/{}{}'.format(input_dir, images, set, year)
        mscoco.mscoco_to_voc(anno,img,output_dir,set)

if __name__ == '__main__':
    main()