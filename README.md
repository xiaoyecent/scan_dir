# scan_dir

py版本御剑扫描器    win下正常  ubuntu下略卡(虚拟机...)  速度较快(threading模块+Queue守护线程数据) 较稳定

```
Usage: scan_dir.py [options]

Options:
  -h, --help            show this help message and exit
  -u INPUT_URL, --url=INPUT_URL
                        the url you wan to scan dir
  -o OUTFILE, --out=OUTFILE
                        output filename
  -s THREADCOUNT, --speed=THREADCOUNT
                        the thread_count
  -d DICTNAME, --dict=DICTNAME
                        dict filename
```

-u -d参数必须指明 -s -o默认为60线程 存在的目录保存在result.txt
