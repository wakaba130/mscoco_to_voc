##
# coding:utf-8
##

import json
import cv2
import os
import create_xml
import argparse

#select_categories = []

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('anno_json',type=str)
    parser.add_argument('images_dir',type=str)
    parser.add_argument('output_dir',type=str)
    parser.add_argument('--view', choices=('on', 'off'), default='off')
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

# select category name
def category(categories,category_id):
    cate = None
    for c in categories:
        if c['id'] == category_id:
            cate = c['name']
    return cate

# draw rectangle and annotation name
def view_annotation(img_name,rect_list,categories):
    if not os.path.isfile(img_name):
        return None

    img = cv2.imread(img_name)

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

    with open(args.anno_json,'r') as fp:
        json_s = json.load(fp)

    categories = json_s['categories']

    image_id_list_buf = []
    for name in json_s['annotations']:
        id = int(name['image_id'])
        image_id_list_buf.append(id)

    image_id_list = list(set(image_id_list_buf))
    image_id_list.sort()
    del image_id_list_buf

    if args.view == 'on':
        cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)

    for id in image_id_list:
        cnt = 0
        rect_list = []
        label_list = []
        for name in json_s['annotations']:
            if id == int(name['image_id']):
                rect_list.append({'id':id, 'category_id':name['category_id'],'rect':name['bbox']})
                cate = category(categories,name['category_id'])
                label_list.append(create_xml.LABEL(cate, 'None', 0, 0, name['bbox']))
                cnt += 1

        print('id {:012d} cnt : {:03d}'.format(id,cnt))

        xml_name = '{}/COCO_train2014_{:012d}.xml'.format(args.output_dir, id)
        create_xml.create_pascalVOC(label_list,xml_name)

        if args.view == 'on':
            img_name = '{}/COCO_train2014_{:012d}.jpg'.format(args.images_dir, id)
            img = view_annotation(img_name,rect_list,categories)
            cv2.imshow('img',img)
            if cv2.waitKey(30) == 27:
                break

    if args.view == 'on':
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()