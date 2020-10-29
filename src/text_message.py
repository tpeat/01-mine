from py_imessage import imessage
import time

def text_message():
    phone = "6154158422"

    if not imessage.check_compatibility(phone):
        print("Not an iPhone")

    guid = imessage.send(phone, "hi octopussy")

# Let the recipient read the message
    time.sleep(5)
    resp = imessage.status(guid)

    print(f'Message was read at {resp.get("date_read")}')

text_message()