##
# coding:utf-8
##

import os
import shutil
import glob
import time
from progressbar import ProgressBar
import argparse

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('images_dir', type=str)
    parser.add_argument('output_dir', type=str)
    args = parser.parse_args()

    if not os.path.isdir(args.images_dir):
        print('Error mscoco_img : images_dir is exist.')
        exit()

    return args

def main():
    print('copy jpeg file')

    args = argparser()

    if os.path.isdir(args.output_dir):
        print('Error mscoco_img : output_dir is exist.')
        exit()
    else:
        os.mkdir(args.output_dir)

    jpg_list = glob.glob('{}/*.jpg'.format(args.input_dir))
    bar = ProgressBar(0,len(jpg_list))
    cnt = 0
    for jpg_name in jpg_list:
        j_path,j_name = os.path.split(jpg_name)
        shutil.copyfile(jpg_name, '{}/{}'.format(output_dir, j_name))
        bar.update(cnt)
        time.sleep(0.1)
        cnt += 1

if __name__ == '__main__':
    main()