# mscoco_to_voc

## 本プログラムについて

mscocoのデータセットのアノテーションのフォーマット（.json）を
Pascal VOCのデータセットのフォーマット（.xml）に変換するコード

## 動作確認バージョン

+ ubuntu 16.04 LTS
+ python >= 3.5.2
+ OpenCV >= 3.2.0

## install

```Shell
$ sudo pip3 install progressbar2
$ sudo pip3 install wget
$ sudo apt-get install unzip
```

## 実行方法

```
$python3 main.py --help
usage: main.py [-h] [--input_dir INPUT_DIR] [--output_dir OUTPUT_DIR]
               [--year {2014,2017}] [--rect_thr RECT_THR]
               [--name_length NAME_LENGTH] [--view {on,off}]

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
  --name_length NAME_LENGTH
                        File name size exp[000000000001.jpg = 12] default:12
  --view {on,off}       Drawing to confirm the image
```

`--name_length`は、画像やXMLの名前の長さを入力します。`000000000001.jpg`の長さは拡張子を含まずに12桁に
なるので、12と設定します。自作のデータセットを作成して、連番名の文字数を変更したときなどに指定してください。

### 例) オプション指定なし

```bash
python3 main.py
```

+ 入力データセットのディレクトリは、プロジェクト直下に作成されます
+ 出力ディレクトリは、プロジェクト直下に作成されます
