# mscoco_to_voc

## Description

mscocoのデータセットのアノテーションのフォーマット（.json）をChainerCV用のPascal VOCのデータセットのフォーマット（.xml）に変換するコード

## Execution environment

+ ubuntu 16.04 LTS
+ python3.5.2
+ OpenCV3.2.0
+ progressbar2
  + if you install `sudo pip3 install progressbar2`

## install apt

```
sudo apt-get install wget unzip
```

## Execution method

```bash
python3 -m mscoco.mscoco [--view {on,off}] [--out_voc_dir {VOC2007,VOC2012}] [{train,trainval,test,val}] [anno_json] [images_dir] [output_dir]
```

+ [--view {on,off}]
+ [--out_voc_dir {VOC2007,VOC2012}]
+ [{train,trainval,test,val}]
+ [anno_json]
+ [images_dir]
+ [output_dir]