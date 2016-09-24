import urllib
import re
import time
import os



import urllib
import re
import time
import sys

ls = ["PIH","aapl","srpt","","abc","WDC"]

def screening(s):
    t = time.asctime(time.localtime(time.time()))
    i = 0
    change_float={}
    change_float['time'] = t
    
    try:
        url = "https://www.google.com/finance?authuser=0&q="+ s + "&ei=qxjiV5CkDsaFmAHBqZq4Bg"
        htmlfile = urllib.urlopen(url)
        htmltext = htmlfile.read()
        regex = '<span (.*) id="ref_(.*)_cp">(.*)</span>'
        pattern = re.compile(regex)
        change_raw = re.findall(pattern,htmltext)
        change = str(change_raw).split(",")[2]
        change_float= float(re.sub('[^A-Za-z0-9.-]+', '', change))
        if i%100==0:
            print change_float
        i+=1
    except:
        print s," is not found" 
        print url
    return change_float

from Queue import Queue
from threading import Thread

class DownloadWorker(Thread):
   def __init__(self, queue):
       Thread.__init__(self)
       self.queue = queue

   def run(self):
       while True:
           # Get the work from the queue and expand the tuple
           stock = self.queue.get()
           screening(stock)
           self.queue.task_done()

def main():
   ts = time.time()
   #client_id = os.getenv('IMGUR_CLIENT_ID')
   #if not client_id:
    #   raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    
   
   stocks = ["PIH","aapl","srpt","","abc","WDC"]
   # Create a queue to communicate with the worker threads
   queue = Queue()
   # Create 8 worker threads
   for x in range(8):
       worker = DownloadWorker(queue)
       # Setting daemon to True will let the main thread exit even though the workers are blocking
       worker.daemon = True
       worker.start()
   # Put the tasks into the queue as a tuple
   for stock in stocks:
       #logger.info('Queueing {}'.format(stock))
       queue.put(stock)
   # Causes the main thread to wait for the queue to finish processing all the tasks
   queue.join()
   print('Took {}'.format(time.time() - ts))


main()


for stock in change_float:
    if change_float[stock] > 30:
        print stock,": ",change_float[stock]
print "completed screening!"

tickerFile = open("stockSymbols.txt")
symbolslist = tickerFile.read()
symbolslist = symbolslist.split("\n")

t = time.time()
screening(symbolslist)
t2 = time.time()
print t2 - t



