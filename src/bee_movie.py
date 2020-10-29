import requests
from bs4 import BeautifulSoup
from py_imessage import imessage
import time


def bee_movie():
    response = requests.get("https://gist.githubusercontent.com/MattIPv4/045239bc27b16b2bcf7a3a9a4648c08a/raw/2411e31293a35f3e565f61e7490a806d4720ea7e/bee%2520movie%2520script")
    soup = BeautifulSoup(response.content, "lxml")
    words = soup.find('p')
    conv = words.text #changes data type to strings, otherwise its like bs4.element.tag
    new = conv.split() #split strings by whitespace into a list
    #phone = "9196013991"
    for each in new:
        #imessage.send(phone, each) attempt to send the messgae with each word
        time.sleep(.5) #and delay each words by one second
        print(each)
bee_movie()  
#while True:
    #time.sleep(1)

def text_message():
    phone = "9196013991"
    if not imessage.check_compatibility(phone):
        print("Not an iPhone")
    guid = imessage.send(phone, bee_movie())
    resp = imessage.status(guid)
    print(f'Message was read at {resp.get("date_read")}')

