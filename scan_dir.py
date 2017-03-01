'''
@author: xiaoye
'''
#coding: utf-8
import requests
import sys
import threading
#import time
import Queue
from optparse import OptionParser

'''reload(sys)
sys.setdefaultencoding('utf8')'''

class Doscan(threading.Thread):
    def __init__(self, que):
        threading.Thread.__init__(self)
        self._que = que
        
    def run(self):
        while not self._que.empty():
            d = self._que.get()
            try: 
                r = requests.get(url + d, headers=headers, timeout=3)
                sys.stdout.write(d + ' is scan  status:' + str(r.status_code) + '\n')
                if r.status_code == 200:
                    with open(option.outfile, 'a') as f:
                        f.write(url + d + '\n')
            except:
                pass
    
def main():
    thread = []
    thread_count = option.threadcount
    que = Queue.Queue()
    
    with open(option.dictname, 'r') as f:
        for d in f.readlines():
            d = d.strip('\n')
            que.put(d)
    
    for i in range(thread_count):
        thread.append(Doscan(que))
    
    for i in thread:
        i.start()
    
    for i in thread:
        i.join()
        
if __name__ == '__main__':
    parse = OptionParser()
    parse.add_option('-u', '--url', dest='input_url', type='string', help='the url you wan to scan dir')
    parse.add_option('-o', '--out', dest='outfile', type='string', help='output filename', default='result.txt')
    parse.add_option('-s', '--speed', dest='threadcount', type='int', default=60, help='the thread_count')
    parse.add_option('-d', '--dict', dest='dictname', type='string', help='dict filename')
    (option, args) = parse.parse_args()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    url = option.input_url
    main()
            

