#This will be the main file

import requests
from bs4 import BeautifulSoup
import time

data = []

def get_price():
    r = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
    soup = BeautifulSoup(r.content, 'lxml') 
    job_elems = soup.find_all('span', attrs={"data-reactid": "50"})
    for job_elem in job_elems:
        output = job_elem.text
    return output

while True:
    temp = float(get_price())
    data.append(get_price())
    print(data)


# not sure why lxml wasn't working, bc now it is
#html.parser also works as the second parameter

#from twisted.internet import task, reactor

#timeout = 60.0 # Sixty seconds

#def doWork():
    #print('working')
    #job_elems = soup.find_all('span', attrs={"data-reactid": "50"})
    #for job_elem in job_elems:
        #output = job_elem.text
        #print(output)
    #pass

#l = task.LoopingCall(doWork)
#l.start(timeout) # call every sixty seconds

##reactor.run()