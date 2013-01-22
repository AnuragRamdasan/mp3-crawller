from downloader import D 

global queue
global DOWNLOAD_START
DOWNLOAD_START = True
queue = set()


def addUrl(url):
    p = open('all.txt', 'a')
    p.write(url)
    p.close()
    global queue, DOWNLOAD_START
    queue.add(url)
    if DOWNLOAD_START:
        D().start()
    DOWNLOAD_START = False
    

def getUrl():
    return queue.pop()

def getQueue():
    for queue in self.queue:
        print queue
            
    
