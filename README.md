# mscoco_to_voc

## Description

mscocoのデータセットのアノテーションのフォーマット（.json）をChainerCV用のPascal VOCのデータセットのフォーマット（.xml）に変換するコード

## Execution environment

+ ubuntu 16.04 LTS
+ python3.5.2
+ OpenCV3.2.0
+ progressbar2
  + if you install `sudo pip3 install progressbar2`

## Execution method

```bash
python3 mscoco.py [annotation_json_file] [images_dir] [output_dir] --view [on/off]
```

+ annotation_json_file
+ images_dir
+ output_dir
+ [option] view 
