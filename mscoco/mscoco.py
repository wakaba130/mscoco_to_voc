##
# coding:utf-8
##

import json
import cv2
import os
import create_xml
import argparse
from progressbar import ProgressBar

voc_bbox_label_names = ('aeroplane',
                        'bicycle',
                        'bird',
                        'boat',
                        'bottle',
                        'bus',
                        'car',
                        'cat',
                        'chair',
                        'cow',
                        'diningtable',
                        'dog',
                        'horse',
                        'motorbike',
                        'person',
                        'pottedplant',
                        'sheep',
                        'sofa',
                        'train',
                        'tvmonitor')

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('anno_json',type=str)
    parser.add_argument('images_dir',type=str)
    parser.add_argument('output_dir',type=str)
    parser.add_argument('--view', choices=('on', 'off'), default='off')
    parser.add_argument('--out_voc_dir',choices=('VOC2007','VOC2012'), default='VOC2007')
    #parser.add_argument('--area',type=int,default=-1) #add annotation rect threshold
    args = parser.parse_args()

    if os.path.isdir(args.output_dir):
        print('argparser error : output_dir is exist.')
        exit()
    else:
        os.mkdir(args.output_dir)

    if not os.path.isfile(args.anno_json):
        print('argparser error : annotation json is not exist.')
        exit()

    return args

# get category name
def category(categories,category_id):
    cate = None
    cate_buf = [c for c in categories if c['id'] == category_id]
    if len(cate_buf) > 0:
        cate = cate_buf[0]['name']
    return cate

# select category name
def select_category(categories, category_id):
    cate = None
    cate_buf = [c for c in categories if c['id'] == category_id]
    if len(cate_buf) > 0:
        if cate_buf[0]['name'] in voc_bbox_label_names:
            cate = cate_buf[0]['name']
    return cate

# draw rectangle and annotation name
def view_annotation(img,rect_list,categories):
    for rec in rect_list:
        x = int(rec['rect'][0])
        y = int(rec['rect'][1])
        xw = x + int(rec['rect'][2])
        yh = y + int(rec['rect'][3])
        cv2.rectangle(img, (x, y), (xw, yh), (0, 0, 255), 2)

        cate = category(categories, int(rec['category_id']))
        if cate is not None:
            cv2.putText(img, cate, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 1, 2)

    return img

def main():
    print('__mscoco_to_PascalVOC__')

    args = argparser()

    print('-- loading annotation json --')
    with open(args.anno_json,'r') as fp:
        json_s = json.load(fp)

    categories = json_s['categories']

    print('-- create index list --')
    image_id_list_buf = []
    for name in json_s['annotations']:
        id = int(name['image_id'])
        image_id_list_buf.append(id)

    image_id_list = list(set(image_id_list_buf))
    image_id_list.sort()
    del image_id_list_buf

    if args.view == 'on':
        cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)

    bar = ProgressBar(0,len(image_id_list)-1)

    print('-- output xmls --')
    count = 0
    for id in image_id_list:
        rect_list = []
        label_list = []
        for name in json_s['annotations']:
            if id == int(name['image_id']):
                #cate = category(categories,name['category_id'])
                cate = select_category(categories,name['category_id'])
                if cate is not None:
                    rect_list.append({'id': id, 'category_id': name['category_id'], 'rect': name['bbox']})
                    label_list.append(create_xml.LABEL(cate, 'Unspecified', 0, 0, name['bbox']))

        bar.update(count)
        count += 1

        if len(label_list) > 0:
            sp_dir = args.images_dir.split('/')
            sp_dir_name = sp_dir[len(sp_dir) - 1]

            img_name = '{}/COCO_{}_{:012d}.jpg'.format(args.images_dir, sp_dir_name, id)
            sp_img_name = os.path.split(img_name)

            if os.path.isfile(img_name):
                img = cv2.imread(img_name)
                h,w,c = img.shape
                img_size = create_xml.IMAGE_SIZE(w,h,c)

                xml_name = '{}/COCO_{}_{:012d}.xml'.format(args.output_dir, sp_dir_name, id)
                create_xml.create_pascalVOC(sp_dir_name,sp_img_name[1],img_size,label_list,xml_name)

                if args.view == 'on':
                    vimg = view_annotation(img,rect_list,categories)
                    cv2.imshow('img',vimg)
                    if cv2.waitKey(30) == 27:
                        break

    if args.view == 'on':
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()