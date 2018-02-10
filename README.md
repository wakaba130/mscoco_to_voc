# mscoco_to_voc

## Description

mscocoのデータセットのアノテーションのフォーマット（.json）をChainerCV用のPascal VOCのデータセットのフォーマット（.xml）に変換するコード
chainercvは、０．６．０のバージョンのみ対応

## Execution environment

+ ubuntu 16.04 LTS
+ python3.5.2
+ OpenCV3.2.0
+ progressbar2
  + if you install `sudo pip3 install progressbar2`

## install apt

```bash
$ sudo apt-get install wget unzip
```

## Execution method

```bash
$ python3 main.py --help
usage: main.py [-h] [--input_dir INPUT_DIR] [--output_dir OUTPUT_DIR]
               [--year {2014,2017}] [--rect_thr RECT_THR] [--view {on,off}]

optional arguments:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR
                        Downloaded data set directory
  --output_dir OUTPUT_DIR
                        Destination directory
  --year {2014,2017}    Designation of data set to be converted (in 2014 or in
                        2017)
  --rect_thr RECT_THR   Designation of minimum size of width and height of
                        anonation rectangle
  --view {on,off}       Drawing to confirm the image
```

### Example) Execute no optional

```bash
python3 main.py
```

+ The input directory is created directly under the project
+ The output directory is created directly under the project
