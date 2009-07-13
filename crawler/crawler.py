#!/usr/bin/python

from HTMLParser import HTMLParser
import urllib
import sys
import re

import time
import datetime


class myParser(HTMLParser):


    viewedQueue = []
    instQueue = []
    totali_links = []

    def __init__(self, url):
       # self.baseUrl = url[:url.rfind('/')]
        self.baseUrl=url
        HTMLParser.__init__(self)
    
    def abc(self):
	print "pranav"	 	
    def reset(self):
        self.urls = set()
        HTMLParser.reset(self)

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == 'a':
            if attrs[0][0] == 'href':
                if attrs[0][1].find(':') == -1:
                    # we need to add the base URL.
              #      self.urls.add(self.baseUrl + '/' + attrs[0][1])
                    print "the base url is" + self.baseUrl
                    temp = self.baseUrl  + attrs[0][1]
                    #temp = self.baseUrl + '/' + attrs[0][1]
                    if temp != '':
                        if re.match('http://tamil.webdunia.com/',temp):
                           
                            self.instQueue.append(temp)
                            self.totali_links.append(temp)
                            print "\nadding ",temp
                          #  if re.match('http://tamil.webdunia.com',temp):
                           #     self.instQueue.append(temp)
                           #     self.totali_links.append(temp)
                            #    print "\ntotali found ",temp
                           # if re.match('http://tamil.webdunia.com',temp):
                           #     self.instQueue.append(temp)
                            #    self.totali_links.append(temp) 
                             #   print "\ntotali found ",temp
                        else:
                            print "\nignored ",temp
                else:
               #     self.urls.add(attrs[0][1])
                    temp = attrs[0][1]
               #     self.instQueue.append(temp)
                    print "\nignored ",temp

    def get_next_link( self ):
        if self.instQueue == []:
            return ''
        else:
            return self.instQueue.pop(0)

    def get_next_totali( self ):
        if self.totali_links == []:
            return ''
        else: 
            return self.totali_links.pop(0)

def main():

    url = 'http://tamil.webdunia.com'
    p = myParser(url)
    n = 0
    startTime = time.time()
#    while url != '':
    while ((n < 2) & (url != '')):
        print "\nChecking ",url
        s = urllib.urlopen(url)
        data = s.read()
        p.feed(data)
        url= p.get_next_link()
        n = n + 1 

    print "\ndone " 
    
    r = 0

    
    
    print "\n total links found ... "
    totali = p.get_next_totali()
    while totali != '':
        #fout.write(totali + '\n')
        totali = p.get_next_totali()  
        r = r + 1
        
    #fout.close()
    elapsedTime = time.time() - startTime
  #  t = datetime.time(0,0,int(elapsedTime), (elapsedTime%1)*1000)
  #  print t.isoformat()
    print "\n\n ",int(elapsedTime/3600)," Hrs",int( ((elapsedTime/60)%60) )," Mins",int(elapsedTime%60)," Secs elapsed";
    print "\ndund per second : ",int(r/elapsedTime) 


#    urllist = p.urls._data.keys()
#    urllist.sort()
#    print '\n'.join(urllist)
if __name__ == "__main__":
    main()
