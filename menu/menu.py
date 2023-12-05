from time import sleep
from colorama import Fore as color
import sys, os



def banner():
    print(color.GREEN+"""

███╗░░░███╗ ███╗░░██╗ ░█████╗ ░███╗░░██╗ ███████╗ 
████╗░████║ ████╗░██║ ██╔══██╗ ████╗░██║ ██╔════╝ 
██╔████╔██║ ██╔██╗██║ ██║░░██║ ██╔██╗██║ █████╗░░ 
██║╚██╔╝██║ ██║╚████║ ██║░░██║ ██║╚████║ ██╔══╝░░ 
██║░╚═╝░██║ ██║░╚███║ ╚█████╔╝ ██║░╚███║ ███████╗ 
╚═╝░░░░░╚═╝ ╚═╝░░╚══╝ ░╚════╝ ░╚═╝░░╚══╝ ╚══════╝ 
                                                               """)

    sleep(0.1)

    print(color.BLUE+"""
######################################################
||| Developer: None   /\/\/\/\/\/\/\   version 2.0 |||                
######################################################             
""")
    sleep(0.1)


def menu_respaws():
    try:
        print(color.RED+"[1] "+ color.LIGHTYELLOW_EX+"Sms-Bomber")
        print(color.CYAN+"---------------------")
        sleep(0.1)
        
        print(color.RED+"[0] "+ color.LIGHTYELLOW_EX+"Exit")
        print(color.CYAN+"---------------------")
        sleep(0.1)
    except:
        print(color.RED+"[-] Something Went Wrong....")
        sleep(1)
        sys.exit()
