##
# coding:utf-8
##

import os
import sys
import wget
import argparse
import subprocess
from mscoco import mscoco

### dounload dataset urls ###
train_2014_url = 'http://images.cocodataset.org/zips/train2014.zip'
val_2014_url = 'http://images.cocodataset.org/zips/val2014.zip'

train_2017_url = 'http://images.cocodataset.org/zips/train2017.zip'
val_2017_url = 'http://images.cocodataset.org/zips/val2017.zip'

anno_2014_url = 'http://images.cocodataset.org/annotations/annotations_trainval2014.zip'
anno_2017_url = 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip'

### input sub dirs ###
annotations = 'annotations'
images = 'images'

def argparser():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir',type=str,
                        default='{}/input_dir'.format(this_dir),
                        help='Downloaded data set directory')
    parser.add_argument('--output_dir', type=str,
                        default='{}/output_dir'.format(this_dir),
                        help='Destination directory')
    parser.add_argument('--year', choices=('2014', '2017'),default='2014',
                        help='Designation of data set to be converted (in 2014 or in 2017)')
    parser.add_argument('--rect_thr', type=int, default=15,
                        help='Designation of minimum size of width and height of anonation rectangle')
    parser.add_argument('--view', choices=('on', 'off'), default='off',
                        help='Drawing to confirm the image')

    return parser.parse_args()

def check_dataset(input_path,year):
    # check dataset dir
    if not os.path.isdir('{}'.format(input_path)):
        os.makedirs(input_path)

    # check annotation file
    input_full_path = os.path.abspath(input_path)
    print('Full Path = {}'.format(input_full_path))
    if not os.path.isfile('{}/{}/instances_train{}.json'.format(input_path, annotations, year)):
        if not os.path.isfile('{}/annotations_trainval{}.zip'.format(input_path,year)):
            if year == '2014':
                #subprocess.check_call(['wget', '-c', anno_2014_url], cwd=input_full_path)
                wget.download(anno_2014_url,out=input_full_path)
            else:
                #subprocess.check_call(['wget', '-c', anno_2017_url], cwd=input_full_path)
                wget.download(anno_2017_url,out=input_full_path)
        subprocess.check_call(['unzip', '{}/annotations_trainval{}.zip'.format(input_path, year)], cwd=input_full_path)

    # check train data
    if not os.path.isdir('{}/{}/train{}'.format(input_full_path, images, year)):
        if not os.path.isfile('{}/train{}.zip'.format(input_full_path, year)):
            if year == '2014':
                #subprocess.check_call(['wget', '-c', train_2014_url], cwd=input_full_path)
                wget.download(train_2014_url, out=input_full_path)
            else:
                #subprocess.check_call(['wget', '-c', train_2017_url], cwd=input_full_path)
                wget.download(train_2017_url, out=input_full_path)

        if not os.path.isdir('{}/{}'.format(input_full_path, images)):
            os.mkdir('{}/{}'.format(input_full_path, images))
        subprocess.check_call(
            ['unzip', '{}/train{}.zip'.format(input_full_path, year)],
            cwd='{}/{}'.format(input_full_path, images))

    # check val data
    if not os.path.isdir('{}/{}/val{}'.format(input_path, images, year)):
        if not os.path.isfile('{}/val{}.zip'.format(input_full_path, year)):
            if year == '2014':
                #subprocess.check_call(['wget', '-c', val_2014_url], cwd=input_full_path)
                wget.download(val_2014_url, out=input_full_path)
            else:
                #subprocess.check_call(['wget', '-c', val_2017_url], cwd=input_full_path)
                wget.download(val_2017_url, out=input_full_path)

        subprocess.check_call(
            ['unzip', '{}/val{}.zip'.format(input_full_path, year)],
            cwd='{}/{}'.format(input_full_path, images))

def main():
    args = argparser()

    if os.path.isdir(args.output_dir):
        print('Error : output dir is exist.')
        sys.exit()

    check_dataset(args.input_dir,args.year)

    for set in ['train', 'val']:
        print('== output {} =='.format(set))
        anno = '{}/{}/instances_{}{}.json'.format(args.input_dir, annotations, set, args.year)
        img = '{}/{}/{}{}'.format(args.input_dir, images, set, args.year)
        mscoco.mscoco_to_voc(anno,img,args.output_dir,set, args.rect_thr, args.view)

if __name__ == '__main__':
    main()