import sys, os
import re
import urllib2
import urlparse
import urlQueue

class Crawl():

    global keywordregex, linkregex, downloadnext
    keywordregex = re.compile('<meta\sname=["\']keywords["\']\scontent=["\'](.*?)["\']\s/>')
    linkregex = re.compile('<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')   

    def __init__(self, _url, _meta):
        self.url = _url
        self.meta = _meta
        self.tocrawl = set([self.url])
        self.crawled = set([])
        #self.downloader = Downloader()
        self.DOWNLOAD_FLAG = False
        downloadnext = False

    def start(self):
        global keywordregex, linkregex
        while 1:
            print 'tocrawl : ',len(self.tocrawl)
            print 'crawled : ',len(self.crawled)
            if len(self.crawled) > 1000:
                break
            try:
                crawling = self.tocrawl.pop()
                #print 'Crawling : ', crawling
            except KeyError:
                raise StopIteration
    
            url = urlparse.urlparse(crawling)
    
            try:
                response = urllib2.urlopen(crawling)
            except:
                continue
        
            msg = response.read()
            #print msg
            keywordlist = keywordregex.findall(msg)
            if len(keywordlist) != 0:
                keywordlist = keywordlist[0]
                keywordlist = keywordlist.split(", ")


            links = linkregex.findall(msg)
            self.crawled.add(crawling)
            
            for link in (links.pop(0) for _ in xrange(len(links))):
                #print link
                if link.startswith('/'):
                    link = 'http://' + url[1] + link
                elif link.startswith('#'):
                    link = 'http://' + url[1] + url[2] + link
                elif not link.startswith('http'):
                    link = 'http://' + url[1] + '/' + link
                
                if link.endswith('.mp3') and self.meta.lower() in link.lower():
                    print link, ' = true'
                    urlQueue.addUrl(link)
            
                if link not in self.crawled:
                    if link.startswith(self.url):
                        #print 'added : ', link
                        self.tocrawl.add(link.replace(' ', ''))
            
        print "that's all!"
        
        
s = Crawl('http://mp3skull.com/', 'gangnam')
s.start()
