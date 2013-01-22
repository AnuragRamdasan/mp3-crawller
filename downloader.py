import urllib2
from datetime import datetime
import threading
import urlQueue

class D(threading.Thread):
    
    def run(self):
        #print self.getQueue()
        while len(urlQueue.queue):
            url = urlQueue.getUrl()
            print 'URL : ', url
            file_name = url.split('/')[-1]
            #if not os.path.isfile(file_name):
            try:
                u = urllib2.urlopen(url)
            except:
                continue
            f = open(file_name, 'wb')
            meta = u.info()
            print url
            print meta
                #file_size = int(meta.getheaders("Content-Length")[0])
            print "Downloading: %s" % (file_name)
            print datetime.time(datetime.now())
                #f.write(u.read())
                #file_size_dl = 0
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break
            
                    #file_size_dl += len(buffer)
                f.write(buffer)
                print "Downloading: %s" % (file_name) 
            f.close()
            p = open('downloaded.txt', 'a')
            p.write(file_name)
            p.close()
        print datetime.time(datetime.now())

